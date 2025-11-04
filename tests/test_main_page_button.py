import re
import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("min_price", [(1000)])

def test_search_table_price(min_price):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context_search = browser.new_context()
        page_search = context_search.new_page()

        page_search.goto("https://lumierecreation.com", timeout=60000)

        eplore_link = page_search.locator("div.banner__buttons a").first
        eplore_link.click()

        page_search.wait_for_timeout(3000)
        
        first_item_price = page_search.locator("div.price").first.locator("div > div > span").nth(1).inner_text()
        match = re.search(r"([\d,]+\.?\d*)", first_item_price)

        assert match, f"你也没标价啊: {first_item_price}"

        price_value = float(match.group(1).replace(",", ""))
        print(f"你的标价: {price_value}")

        assert price_value >= min_price, f"这么便宜，不够奸商，重卖: {price_value} CAD"

        context_search.close()
        browser.close()
        #
