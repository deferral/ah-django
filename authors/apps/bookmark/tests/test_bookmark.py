from rest_framework.reverse import reverse
from .base_test import BookmarkTestBase
from rest_framework import status


class TestBookmarkArticle(BookmarkTestBase):
    """Tests for bookmarking an article"""

    def test_non_existing_slug(self):
        """ Testing for non existent bookmarks"""
        slug = 'non_existing_article'
        bookmark_article_url = reverse('bookmark:bookmark-article',
                                       kwargs={
                                           'slug': slug
                                       })
        response = self.client.post(bookmark_article_url, format="json")
        self.assertEqual(
            response.content,
            b'{"detail":"Article with slug non_existing_article nonexistent"}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_bookmark_toggle_feature(self):
        """ Test for toggle between mark and unmark bookmark"""
        self.assertEqual(self.toogle_bookmark_feature()[0].status_code,
                         status.HTTP_201_CREATED)
        self.assertEqual(self.toogle_bookmark_feature()[
                         0].data.get('message', ''), '')
        self.assertEqual(self.toogle_bookmark_feature()[1].status_code,
                         status.HTTP_404_NOT_FOUND)
        self.assertEqual(self.toogle_bookmark_feature()[
                         1].data.get('message', ''), '')

    def test_non_existent_bookmarks(self):
        """ test non existence bookmark """
        response = self.client.get(
            self.bookmark_url,
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + self.token1
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'NO article Bookmarked')

    def test_delete_bookmark(self):
        """ test existing bookmark """
        self.assertEqual(self.toogle_bookmark_feature()[1].status_code,
                         status.HTTP_200_OK)
        self.assertEqual(self.toogle_bookmark_feature()[
                         1].data.get('message', ''), '')
