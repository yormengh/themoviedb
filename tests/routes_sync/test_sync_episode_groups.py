from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


def test_episode_group_details(get_data, assert_data):
    data = get_data("tv_episode_groups/details")
    episode_group_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        episode_groups = tmdb.TMDb().episode_group(episode_group_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/episode_group/{episode_group_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(episode_groups, schemas.EpisodeGroup)
    assert assert_data(episode_groups, data)
