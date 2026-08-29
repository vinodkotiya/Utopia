"""
Exchange a Shopify OAuth authorization code for an admin API access token.

USAGE (PowerShell):
    $env:SHOPIFY_CLIENT_ID     = "your_client_id"
    $env:SHOPIFY_CLIENT_SECRET = "your_client_secret"
    $env:SHOPIFY_CODE          = "your_one_time_code"
    python shopify/get_token.py

NOTES:
- The `code` is single-use and expires a few minutes after it is generated.
  If you get an "invalid_request" error, re-run the OAuth authorize step in a
  browser to obtain a fresh code, then run this again immediately.
- On success the access token is printed and written to shopify/.token
  (this file is git-ignored — do not commit it).
"""

import json
import os
import sys
import urllib.request
import urllib.error

SHOP = "2qsfpz-t4.myshopify.com"
TOKEN_URL = f"https://{SHOP}/admin/oauth/access_token"


def main() -> int:
    client_id = os.environ.get("SHOPIFY_CLIENT_ID")
    client_secret = os.environ.get("SHOPIFY_CLIENT_SECRET")
    code = os.environ.get("SHOPIFY_CODE")

    missing = [
        name
        for name, val in (
            ("SHOPIFY_CLIENT_ID", client_id),
            ("SHOPIFY_CLIENT_SECRET", client_secret),
            ("SHOPIFY_CODE", code),
        )
        if not val
    ]
    if missing:
        print(f"ERROR: missing environment variable(s): {', '.join(missing)}")
        print("Set them first (see the docstring at the top of this file).")
        return 1

    payload = json.dumps(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        TOKEN_URL,
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            data = json.loads(body)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code} from Shopify: {detail}")
        if e.code in (400, 401):
            print(
                "\nHint: the authorization code is likely expired or already used. "
                "Generate a fresh one via the OAuth authorize URL and retry immediately."
            )
        return 2
    except urllib.error.URLError as e:
        print(f"Network error contacting Shopify: {e.reason}")
        return 3

    token = data.get("access_token")
    if not token:
        print(f"Unexpected response (no access_token): {data}")
        return 4

    scope = data.get("scope", "")
    print("SUCCESS")
    print(f"access_token: {token}")
    if scope:
        print(f"granted scopes: {scope}")

    token_path = os.path.join(os.path.dirname(__file__), ".token")
    with open(token_path, "w", encoding="utf-8") as f:
        f.write(token)
    print(f"\nToken saved to {token_path} (git-ignored). Keep it secret.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
