SELECT posts.id, posts.user_id, users.username
FROM posts
JOIN users
ON posts.user_id = users.id

--I want username of user for each post. 