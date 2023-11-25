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


--Using a window function, count the number of comments a post then join that to the user and posts table to show both the username and caption of the post.

SELECT
    users.id,
    users.username,
    posts.caption,
    COUNT(comments.id) OVER (PARTITION BY posts.id) AS comment_count
FROM
    posts
	
LEFT JOIN
    users ON posts.user_id = users.id
LEFT JOIN
    comments ON posts.id = comments.post_id

