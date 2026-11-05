"""Real-browser test for a completed Rock Paper Scissors round and replay."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_real_game_round_and_replay(page: Page, live_server, monkeypatch):
    """Verify two independent rounds using the real winner function."""

    computer_moves = iter(["paper", "paper"])
    monkeypatch.setattr(web.random, "choice", lambda _moves: next(computer_moves))

    page.goto(live_server)

    # First round: Rock loses to Paper.
    page.get_by_role("button", name="Rock", exact=True).click()

    expect(page.get_by_text("You chose", exact=True)).to_be_visible()
    expect(page.get_by_text("Computer chose", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Computer wins")).to_be_visible()
    expect(page.locator('[data-outcome="lose"]')).to_have_count(1)

    # Second round: Scissors beats Paper.
    page.get_by_role("button", name="Scissors", exact=True).click()

    expect(page.get_by_text("You chose", exact=True)).to_be_visible()
    expect(page.get_by_text("Computer chose", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="You win!")).to_be_visible()
    expect(page.locator('[data-outcome="win"]')).to_have_count(1)
