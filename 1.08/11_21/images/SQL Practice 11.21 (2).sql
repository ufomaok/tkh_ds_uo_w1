--Please get all post ids, their captions, and the hashtags related to the post. Each hashtag has a single `title`. You may need to join multiple tables!

-- SELECT hashtags.id, hashtags.title, posts.id, posts.caption
-- FROM posts
-- LEFT JOIN hashtags_posts ON posts.id = hashtags_posts.post_id
-- INNER JOIN hashtags ON hashtags.id = hashtags_posts.hashtag_id

--Using subqueries, try to filter out comments that are shorter than the average lenght. In other words, we want only comments which are longer than average.

-- SELECT contents
-- FROM comments
-- WHERE LENGTH(contents) > (SELECT AVG(LENGTH(contents))
-- 						  FROM comments)


--