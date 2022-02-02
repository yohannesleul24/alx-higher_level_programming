-- SQL  script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT DISTINCT tv_genres.name
FROM tv_shows
	LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
	LEFT JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
WHERE tv_genres.name NOT IN (
	SELECT tv_genres.name
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_genres.id=tv_show_genres.genre_id
	AND tv_show_genres.show_id=tv_shows.id
	AND tv_shows.title='Dexter')
ORDER BY tv_genres.name;
