
# Convert destination.md entries to HTML files using TEMPLATE.html
# Includes SEO enhancements: FAQ schema, meta keywords, sr-only text, details element

$ErrorActionPreference = 'Continue'
$templatePath = "d:\temp\blog final\output\TEMPLATE.html"
$destPath = "d:\temp\blog final\output\destination.md"
$outputDir = "d:\temp\blog final\output"

# Read template
$template = Get-Content $templatePath -Raw

# Read destination.md
$destContent = Get-Content $destPath -Raw

# Split into entries
$entries = $destContent -split '(?m)^=== #\d+ ===' | Where-Object { $_.Trim() -ne '' -and $_ -match 'TARGET:' }

Write-Host "Found $($entries.Count) entries to process..."

$processed = 0
$skipped = 0

foreach ($entry in $entries) {
    # Extract TARGET
    if ($entry -notmatch 'TARGET:\s*(.+\.html)') { $skipped++; continue }
    $target = $Matches[1].Trim()
    
    # Extract TITLE
    if ($entry -notmatch 'TITLE:\s*(.+)') { $skipped++; continue }
    $title = $Matches[1].Trim()
    
    # Extract DATE
    if ($entry -notmatch 'DATE:\s*(.+)') { $skipped++; continue }
    $dateStr = $Matches[1].Trim()
    
    # Convert date to ISO
    try {
        $dateObj = [datetime]::ParseExact($dateStr, "MMMM d, yyyy", [System.Globalization.CultureInfo]::InvariantCulture)
        $dateISO = $dateObj.ToString("yyyy-MM-dd")
    } catch {
        $dateISO = "2027-01-01"
    }
    
    # Extract CONTENT
    if ($entry -notmatch '(?s)CONTENT:\s*\n(.+)') { $skipped++; continue }
    $content = $Matches[1].Trim()
    
    if ($content.Length -lt 100) { $skipped++; continue }
    
    # Generate SLUG (filename without .html)
    $slug = $target -replace '\.html$', ''
    
    # Generate BREADCRUMB (shortened title - first 40 chars or to first colon)
    $breadcrumb = $title
    if ($title -match '^(.+?):\s') { $breadcrumb = $Matches[1] }
    if ($breadcrumb.Length -gt 50) { $breadcrumb = $breadcrumb.Substring(0, 47) + '...' }
    
    # Generate META_DESCRIPTION (first ~155 chars of content)
    $firstPara = ($content -split '\n\n')[0] -replace '\*\*', '' -replace '\*', ''
    $metaDesc = $firstPara.Substring(0, [Math]::Min(155, $firstPara.Length))
    if ($metaDesc.Length -eq 155) { $metaDesc = $metaDesc.Substring(0, $metaDesc.LastIndexOf(' ')) + '...' }
    $metaDesc = $metaDesc -replace '"', '&quot;' -replace '<', '' -replace '>', ''
    
    # Split content into INTRO and BODY at first ## heading
    $introEnd = $content.IndexOf("`n## ")
    if ($introEnd -lt 0) { $introEnd = $content.IndexOf("`n## ") }
    
    if ($introEnd -gt 0) {
        $contentIntro = $content.Substring(0, $introEnd).Trim()
        $contentBody = $content.Substring($introEnd).Trim()
    } else {
        # No ## found - put first 2 paragraphs as intro
        $paras = $content -split '\n\n'
        $contentIntro = ($paras[0..1] -join "`n`n").Trim()
        $contentBody = ($paras[2..($paras.Count-1)] -join "`n`n").Trim()
    }
    
    # --- Convert Markdown to HTML ---
    function Convert-MdToHtml($md) {
        $lines = $md -split '\n'
        $html = @()
        $inList = $false
        
        foreach ($line in $lines) {
            $trimmed = $line.Trim()
            if ($trimmed -eq '') {
                if ($inList) { $html += '</ul>'; $inList = $false }
                continue
            }
            
            # H2
            if ($trimmed -match '^## (.+)') {
                if ($inList) { $html += '</ul>'; $inList = $false }
                $heading = $Matches[1] -replace '\*\*', ''
                $html += "<h2 class=`"text-[clamp(1.2rem,3vw,1.7rem)] leading-[1.3] mt-12 mb-5`" style=`"font-family:var(--font-display);color:var(--text-heading)`">$heading</h2>"
                continue
            }
            
            # H3
            if ($trimmed -match '^### (.+)') {
                if ($inList) { $html += '</ul>'; $inList = $false }
                $heading = $Matches[1] -replace '\*\*', ''
                $html += "<h3 class=`"text-[1.1rem] leading-[1.3] mt-8 mb-3`" style=`"font-family:var(--font-display);color:var(--text-heading)`">$heading</h3>"
                continue
            }
            
            # List item
            if ($trimmed -match '^- (.+)') {
                if (-not $inList) { $html += '<ul class="list-disc pl-6 mb-6 space-y-2" style="color:var(--text-body)">'; $inList = $true }
                $li = $Matches[1]
                # Bold conversion
                $li = $li -replace '\*\*(.+?)\*\*', '<strong>$1</strong>'
                $html += "<li class=`"text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9]`">$li</li>"
                continue
            }
            
            # Regular paragraph
            if ($inList) { $html += '</ul>'; $inList = $false }
            $para = $trimmed
            # Bold conversion
            $para = $para -replace '\*\*(.+?)\*\*', '<strong>$1</strong>'
            $html += "<p class=`"text-[clamp(0.9rem,1.8vw,1.05rem)] font-light leading-[1.9] mb-6`" style=`"color:var(--text-body)`">$para</p>"
        }
        if ($inList) { $html += '</ul>' }
        return ($html -join "`n      ")
    }
    
    $introHtml = Convert-MdToHtml $contentIntro
    $bodyHtml = Convert-MdToHtml $contentBody
    
    # --- Extract FAQ for schema ---
    $faqSchema = ''
    $faqMatches = [regex]::Matches($content, '(?m)^### (.+?)\n\n(.+?)(?=\n\n###|\n\n##|\z)', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    
    # Only get FAQs from the FAQ section
    $faqSection = ''
    if ($content -match '(?s)## Frequently Asked Questions\s*\n(.+)$') {
        $faqSection = $Matches[1]
    }
    
    if ($faqSection) {
        $faqItems = [regex]::Matches($faqSection, '(?m)^### (.+?)\s*\n\n(.+?)(?=\n\n###|\z)', [System.Text.RegularExpressions.RegexOptions]::Singleline)
        if ($faqItems.Count -gt 0) {
            $faqEntries = @()
            foreach ($faq in $faqItems) {
                $q = $faq.Groups[1].Value.Trim() -replace '"', '\"'
                $a = $faq.Groups[2].Value.Trim() -replace '\*\*', '' -replace '\n', ' ' -replace '"', '\"'
                if ($a.Length -gt 300) { $a = $a.Substring(0, 297) + '...' }
                $faqEntries += "{`"@type`":`"Question`",`"name`":`"$q`",`"acceptedAnswer`":{`"@type`":`"Answer`",`"text`":`"$a`"}}"
            }
            $faqSchema = "`n  <script type=`"application/ld+json`">{`"@context`":`"https://schema.org`",`"@type`":`"FAQPage`",`"mainEntity`":[$($faqEntries -join ',')]}</script>"
        }
    }
    
    # --- Generate meta keywords ---
    $keywords = @()
    # Extract key terms from title
    $titleWords = ($title -replace '[^a-zA-Z\s]', '' -split '\s+') | Where-Object { $_.Length -gt 3 }
    $keywords += ($titleWords[0..5] -join ' ').ToLower()
    $keywords += "north vancouver"
    $keywords += "utopia wellness"
    # Add topic-specific keywords
    if ($title -match 'tarot|card') { $keywords += 'tarot reading north vancouver' }
    if ($title -match 'crystal') { $keywords += 'crystal shop north vancouver' }
    if ($title -match 'astrol|zodiac|sign') { $keywords += 'astrology reading north vancouver' }
    if ($title -match 'dream') { $keywords += 'dream interpretation spiritual guidance' }
    if ($title -match 'palm') { $keywords += 'palm reading north vancouver' }
    if ($title -match 'angel') { $keywords += 'angel number spiritual meaning' }
    if ($title -match 'chakra') { $keywords += 'chakra healing energy work' }
    if ($title -match 'meditat') { $keywords += 'meditation spiritual practice' }
    $metaKeywords = ($keywords | Select-Object -Unique) -join ', '
    
    # --- Generate sr-only text ---
    $srOnly = "Psychic readings, tarot card readings, crystal healing, spiritual guidance, North Vancouver metaphysical shop, Utopia Wellness and Gifts, 1826 Lonsdale Ave"
    
    # --- Generate details/summary keywords ---
    $detailsKeywords = $title.ToLower() -replace '[^a-z\s]', ''
    $detailsKeywords += ", spiritual guidance north vancouver, utopia wellness gifts lonsdale, psychic reading, energy healing, crystal shop"
    
    # --- Build final HTML ---
    $html = $template
    $html = $html -replace '\{\{TITLE\}\}', ($title -replace '&', '&amp;')
    $html = $html -replace '\{\{META_DESCRIPTION\}\}', $metaDesc
    $html = $html -replace '\{\{SLUG\}\}', $slug
    $html = $html -replace '\{\{BREADCRUMB\}\}', ($breadcrumb -replace '&', '&amp;')
    $html = $html -replace '\{\{DATE\}\}', $dateStr
    $html = $html -replace '\{\{DATE_ISO\}\}', $dateISO
    $html = $html -replace '\{\{CONTENT_INTRO\}\}', $introHtml
    $html = $html -replace '\{\{CONTENT_BODY\}\}', $bodyHtml
    
    # Insert meta keywords after meta description
    $metaKeywordsTag = "`n  <meta name=`"keywords`" content=`"$metaKeywords`">"
    $html = $html -replace '(<meta name="twitter:description"[^>]+>)', "`$1$metaKeywordsTag"
    
    # Insert FAQ schema before closing body
    if ($faqSchema) {
        $html = $html -replace '</body>', "$faqSchema`n</body>"
    }
    
    # Insert sr-only span and details element before closing article
    $seoBlock = @"

      <span class="sr-only">$srOnly</span>
      <details class="mt-8">
        <summary style="font-size:.85rem;color:var(--violet);cursor:pointer">Related topics covered in this article</summary>
        <p style="font-size:.8rem;color:var(--text-muted);line-height:1.8;margin-top:.5rem">$detailsKeywords</p>
      </details>
"@
    $html = $html -replace '(    </div>\s*</article>)', "$seoBlock`n    </div>`n  </article>"
    
    # Add sr-only CSS if not present (add to head)
    if ($html -notmatch 'sr-only') {
        $srCss = "`n  <style>.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}</style>"
        $html = $html -replace '(</head>)', "$srCss`n</head>"
    }
    
    # Write file
    $outFile = Join-Path $outputDir $target
    [System.IO.File]::WriteAllText($outFile, $html, [System.Text.Encoding]::UTF8)
    $processed++
    
    if ($processed % 50 -eq 0) { Write-Host "  Processed $processed files..." }
}

Write-Host "`nDone! Processed: $processed files. Skipped: $skipped entries."
