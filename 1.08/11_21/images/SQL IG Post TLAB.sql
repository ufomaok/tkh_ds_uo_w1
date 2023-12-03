-- SELECT *
-- -- FROM users;

-- SELECT username,email
-- FROM users
-- WHERE EXTRACT (YEAR FROM created_at) > 2013

-- SELECT COUNT(*) AS total_user_count
-- FROM users

-- SELECT users.id as UID, users.username, posts.created_at, posts.id as PID,
-- COUNT(posts.id) OVER (PARTITION BY users.id) AS posts_counts
-- FROM users
-- LEFT JOIN
-- 	posts on users.id = posts.user_id 
-- WHERE posts.id IS NOT NULL;

SELECT posts.id AS POSTID, MIN(caption_tags.created_at), posts.caption
FROM posts
LEFT JOIN 
	caption_tags on posts.id = caption_tags.id
GROUP BY posts.id













