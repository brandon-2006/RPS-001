# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

The player predicts that Rock versus Paper results in a loss because Paper beats Rock.

Implementation plan:
1. Implement determine_winner(player, computer) in game.py.
2. Handle all nine possible combinations.
3. Return win, lose, or tie from the player's perspective.
4. Display both choices and the correct result.
5. Add nine unit tests, an integration test, and a browser test.
6. Run the full checks and review the code.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: https://github.com/brandon-2006/RPS-001/issues/1
- Pull request / CI: Not created yet.
- Implementation: **Implemented.** `game.py` contains `determine_winner(player, computer)` and handles all nine valid Rock, Paper, Scissors combinations.
- Unit tests: **Passed.** All 9 matchup tests in `tests/test_game.py`.
- Integration tests: **Passed.** All 14 tests in `tests/test_shell.py`, including the real-round integration test.
- Browser tests: **Passed individually.** The new round/replay test, supplied starter test, and four development-refresh tests passed when run separately. The combined six-test browser run repeatedly stalled after the first test.
- Fast checks: **Passed.** Black formatting, Pylint, and 23 non-browser tests passed using `python check.py --fast`.
- Full checks: **Not yet passed.** The combined browser run remains unresolved; do not treat the fast check as the full check.
- Browser observations: Verified a Rock-versus-Paper loss and a Scissors-versus-Paper win, including replay in the real browser test.