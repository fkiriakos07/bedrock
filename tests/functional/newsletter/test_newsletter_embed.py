# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest

from pages.contribute.contribute import ContributePage
from pages.mission import MissionPage
from pages.newsletter.developer import DeveloperNewsletterPage
from pages.newsletter.firefox import FirefoxNewsletterPage
from pages.newsletter.index import NewsletterPage
from pages.newsletter.mozilla import MozillaNewsletterPage
from pages.newsletter.security_privacy_news import SecurityPrivacyNewsletterPage


@pytest.mark.smoke
@pytest.mark.nondestructive
@pytest.mark.parametrize(
    "page_class",
    [
        MissionPage,
        NewsletterPage,
        DeveloperNewsletterPage,
        FirefoxNewsletterPage,
        MozillaNewsletterPage,
        SecurityPrivacyNewsletterPage,
    ],
)
def test_newsletter_default_values(page_class, base_url, selenium):
    page = page_class(selenium, base_url).open()
    page.newsletter.expand_form()
    assert "" == page.newsletter.email
    assert "United States" == page.newsletter.country
    assert not page.newsletter.privacy_policy_accepted
    assert page.newsletter.is_privacy_policy_link_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
@pytest.mark.parametrize(
    "page_class",
    [
        MissionPage,
        ContributePage,
        NewsletterPage,
        DeveloperNewsletterPage,
        FirefoxNewsletterPage,
        MozillaNewsletterPage,
        SecurityPrivacyNewsletterPage,
    ],
)
def test_newsletter_sign_up_success(page_class, base_url, selenium):
    page = page_class(selenium, base_url).open()
    assert not page.newsletter.sign_up_successful
    page.newsletter.expand_form()
    page.newsletter.type_email("success@example.com")
    page.newsletter.select_country("United Kingdom")
    page.newsletter.accept_privacy_policy()
    page.newsletter.click_sign_me_up()
    assert page.newsletter.sign_up_successful


@pytest.mark.smoke
@pytest.mark.nondestructive
@pytest.mark.parametrize(
    "page_class",
    [
        MissionPage,
        ContributePage,
        NewsletterPage,
        DeveloperNewsletterPage,
        FirefoxNewsletterPage,
        MozillaNewsletterPage,
        SecurityPrivacyNewsletterPage,
    ],
)
def test_newsletter_sign_up_failure(page_class, base_url, selenium):
    page = page_class(selenium, base_url).open()
    assert not page.newsletter.is_form_error_displayed
    page.newsletter.expand_form()
    page.newsletter.type_email("failure@example.com")
    page.newsletter.select_country("United Kingdom")
    page.newsletter.accept_privacy_policy()
    page.newsletter.click_sign_me_up(expected_result="error")
    assert page.newsletter.is_form_error_displayed
