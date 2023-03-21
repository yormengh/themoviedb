from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


def test_review_details(get_data, assert_data):
    data = get_data("reviews/details")
    review_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        review = tmdb.TMDb().review(review_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/review/{review_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(review, schemas.Review)
    assert assert_data(review, data)
