from pprint import pprint

from playwright.sync_api import Page, Response, Request, APIRequestContext, APIResponse, expect, Playwright

from tests.utils.constants import BASE_URL


def test_request_response(page: Page):
    response: Response = page.goto(BASE_URL)

    print(response.url)
    print(response.status)
    print(response.ok)

    pprint(response.all_headers())  # Dict[str, str]
    pprint(response.headers_array())  # List[NameValue]

    print(response.body())  # bytes
    print(response.text())  # String obj

    # print(response.json()) # throws if not parseable json

    request: Request = response.request

    print(request.all_headers())
    print(request.method)


def test_api_request(page: Page):
    response: Response = page.goto(BASE_URL)

    api_ctx: APIRequestContext = page.request

    api_response: APIResponse = api_ctx.get('https://api.github.com/')

    print(response.ok)
    print(response.status)
    pprint(api_response.headers_array)
    pprint(api_response.json())

    expect(api_response).to_be_ok()


def test_api_request_context(playwright: Playwright):
    independent_api_ctx = playwright.request.new_context(base_url='...')

    independent_api_ctx.get('your/api/url')