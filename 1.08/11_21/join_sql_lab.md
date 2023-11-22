# Lab Title: SQL JOIN and CTEs

## Objective
The goal of this lab is to provide participants with hands-on experience in using JOIN, Subqueries, and CTEs. Since we have done some practice in class, we will jump straight into the questions!

These might be a bit tricky so take your time! 

## Lab Outline

### 1. Connecting to the Database (5 minutes)
Please make sure you are connected to the database in your PGAdmin4 and have properly loaded the Instagram SQL.


### 2. JOINs practice

Please get all post ids, their captions, and the hashtags related to the post. Each hashtag has a single `title`. You may need to join multiple tables!

![Alt text](images\q1.png)

```sql
SELECT hashtags.id, hashtags.title, posts.id, posts.caption
FROM posts
LEFT JOIN hashtags_posts ON posts.id = hashtags_posts.post_id
INNER JOIN hashtags ON hashtags.id = hashtags_posts.hashtag_id
```
### 3. Subquery Practice

Using subqueries, try to filter out comments that are shorter than the average lenght. In other words, we want only comments which are longer than average.

![Alt text](images\q2.png)

```sql
SELECT contents
FROM comments
WHERE LENGTH(contents) > (SELECT AVG(LENGTH(contents))
						  FROM comments)
```

### 4. CTE Practice

Using a window function, count the number of comments a post then join that to the user and posts table to show both the username and caption of the post.

![Alt text](images\q3.png)