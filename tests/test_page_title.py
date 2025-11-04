from playwright.sync_api import Page, expect

def test_homepage_title(page: Page):
    page.goto("https://lumierecreation.com/")
    expect(page).to_have_title("Transparent Art, Creative Life – Lumière Creation")