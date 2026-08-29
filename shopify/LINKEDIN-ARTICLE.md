The night I published 487 blog posts to a metaphysical shop's Shopify store.

A client came to me with a beautiful problem. Utopia Wellness & Gifts, a metaphysical shop in North Vancouver that has held sacred space since 2004, had built up nearly 500 blog articles. Tarot meanings, astrology guides, crystal healing, dream symbolism, angel numbers, palmistry. A real library of spiritual knowledge, all sitting as static HTML files. The ask was simple to say and hard to do: get all of it live on our Shopify blog. By hand that is weeks of copy-pasting and clicking Publish 487 times, so I stopped clicking and started scripting. By the end of one evening, every article was live.


PART 1: GETTING A SHOPIFY ADMIN API ACCESS TOKEN

You cannot touch a Shopify store's data programmatically until you have been let in. Shopify uses OAuth, and the end goal is a single access token you attach to every request. Here is the exact process.

Step 1 — Register the app. In the store's Developer Dashboard, create a new app record, give it a name, and select only the API access scopes your integration actually needs. For publishing blog articles that is write_content. Requesting the minimum keeps you aligned with least-privilege security, which matters even more on a client's store.

Step 2 — Configure security (the redirect URL). In the app settings, define a redirect URL (a whitelisted URI). This is the address Shopify sends the user back to after they approve the app, and it acts as a security checkpoint. Only URLs you register here can receive the authorization code.

Step 3 — Install the app. Installing it onto the store generates two credentials you will need next: a Client ID (the public identifier) and a Client Secret (the private key, treat it like a password).

Step 4 — Initiate authorization. Build the authorize URL and paste it into a browser:

https://{your-store}.myshopify.com/admin/oauth/authorize?client_id={client_id}&redirect_uri={whitelisted_uri}

After you approve, Shopify redirects you to your redirect URI with a temporary authorization code appended to the URL as a query parameter. Grab it quickly, because it expires within minutes.

Step 5 — Exchange the code for a token. Send a POST request to:

https://{your-store}.myshopify.com/admin/oauth/access_token

with a JSON body containing three fields: client_id, client_secret, and the code from Step 4. You can use Postman, or a few lines of Python:

import json, urllib.request
payload = json.dumps({
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "code": CODE,
}).encode()
req = urllib.request.Request(
    f"https://{SHOP}.myshopify.com/admin/oauth/access_token",
    data=payload, method="POST",
    headers={"Content-Type": "application/json"},
)
token = json.load(urllib.request.urlopen(req))["access_token"]

Shopify returns your access token in the response body. Unlike the code, this token is permanent, which is exactly why I never wrote it into a source file. It lives in an environment variable, and the file it caches to is git-ignored. On a client project, treating credentials carelessly is how you lose a client, so I keep secrets out of the repo and flag when we are done so they can rotate anything that was ever exposed.


PART 2: PUBLISHING HUNDREDS OF ARTICLES DYNAMICALLY

With the token in hand, the rest is talking to the Admin API.

Step 1 — Find the target blog. A store can have multiple blogs, each with its own ID, so list them first with a GET request to /admin/api/2024-10/blogs.json and pick the one you want.

Step 2 — Clean the content before sending. This was the biggest lesson. My source files were full standalone web pages: navigation, footer, inline styles, structured-data scripts, and CTA blocks. Shopify articles want simple semantic HTML: headings, paragraphs, lists, bold, and links. Scripts get stripped and inline styles clash with the theme. So I wrote a small parser that keeps only h2, h3, p, ul, li, strong, and a, drops everything else, and rewrites relative links to absolute utopiastore.ca URLs. I also injected one clean call-to-action in the middle of each article with no styling, so it inherits the store theme perfectly. The rule of thumb: let the Shopify theme own the presentation, and give it clean structure to work with.

Step 3 — Create and publish each article. POST to /admin/api/2024-10/blogs/{blog_id}/articles.json with a body like:

{
  "article": {
    "title": "Your Post Title",
    "body_html": "<p>Clean semantic HTML here...</p>",
    "author": "Utopia Wellness & Gifts",
    "published": true
  }
}

Set published to true to go live immediately, or false to stage drafts and publish in bulk later.

Step 4 — Rate-limit and track progress. Two things make a batch this size reliable. First, rate limiting: Shopify's REST API uses a leaky-bucket limit, so I added a short delay (about 0.6 seconds) between calls and a retry-with-backoff on any 429 Too Many Requests response. No throttling errors across the entire run. Second, a resume log: after each successful post I appended a row to a Markdown tracker with the filename, status, new article ID, and timestamp. On startup the script reads that file and skips anything already marked done, so I can interrupt and restart safely with zero duplicates. When it finished, the tracker showed 487 rows, and Shopify's own article-count endpoint returned exactly 487. Numbers matched. Done.


THE TAKEAWAYS

Ask for the least access you need (write_content for blogs). Guard the secret and token with environment variables and git-ignored files, and rotate on leak. Clean the HTML before you send it, stripping scripts and inline styles so the theme does the styling. Rate-limit and log every step to turn a fragile bulk job into a repeatable, restartable one.

What used to be a multi-day manual chore became a single command I can re-run anytime the client adds new content. A 20-year-old sacred space in North Vancouver now has its entire body of spiritual writing where its customers can actually find it. Sometimes the most magical thing you can do for a metaphysical shop is a little bit of very ordinary automation.

If you are sitting on a pile of content and a Shopify store, the Admin API is genuinely your friend. Questions welcome in the comments.

#Shopify #Python #API #Automation #Ecommerce #Freelance #WebDevelopment
