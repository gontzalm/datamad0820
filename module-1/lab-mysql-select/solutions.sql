-- CHALLENGE #1

SELECT 
    au.au_id AS `AUTHOR ID`,
    au_lname AS `LAST NAME`,
    au_fname AS `FIRST NAME`,
    title AS TITLE,
    pub_name AS PUBLISHER
FROM
    authors AS au
    INNER JOIN titleauthor AS ta ON au.au_id = ta.au_id
    INNER JOIN titles AS t ON ta.title_id = t.title_id
    INNER JOIN publishers AS p ON t.pub_id = p.pub_id
ORDER BY `AUTHOR ID` ASC;

-- CHALLENGE #2

SELECT 
    `AUTHOR ID`,
    `LAST NAME`,
    `FIRST NAME`,
    `PUBLISHER`,
    COUNT(`TITLE`) AS `TITLE COUNT`
FROM
    (SELECT 
        au.au_id AS `AUTHOR ID`,
        au_lname AS `LAST NAME`,
        au_fname AS `FIRST NAME`,
        title AS TITLE,
        pub_name AS PUBLISHER
    FROM
        authors AS au
    INNER JOIN titleauthor AS ta ON au.au_id = ta.au_id
    INNER JOIN titles AS t ON ta.title_id = t.title_id
    INNER JOIN publishers AS p ON t.pub_id = p.pub_id) AS subquery
GROUP BY `AUTHOR ID` , `PUBLISHER`
ORDER BY `AUTHOR ID` DESC;

-- CHALLENGE #3

SELECT
	au.au_id AS `AUTHOR ID`,
    au.au_lname AS `LAST NAME`,
    au.au_fname AS `FIRST NAME`,
    SUM(s.qty) AS `TOTAL`
FROM
	authors AS au
    INNER JOIN titleauthor AS ta ON au.au_id = ta.au_id
    INNER JOIN sales AS s ON ta.title_id = s.title_id
GROUP BY `AUTHOR ID`
ORDER BY `TOTAL` DESC
LIMIT 3;

-- CHALLENGE #4

SELECT
	au.au_id AS `AUTHOR ID`,
    au.au_lname AS `LAST NAME`,
    au.au_fname AS `FIRST NAME`,
    IFNULL(SUM(s.qty), 0) AS `TOTAL`
FROM
	authors AS au
    LEFT JOIN titleauthor AS ta ON au.au_id = ta.au_id
    LEFT JOIN sales AS s ON ta.title_id = s.title_id
GROUP BY `AUTHOR ID`
ORDER BY `TOTAL` DESC;

-- BONUS

SELECT
	au.au_id AS `AUTHOR ID`,
    au.au_lname AS `LAST NAME`,
    au.au_fname AS `FIRST NAME`,
    SUM((s.qty*t.price + t.advance)*t.royalty/100*ta.royaltyper/100) AS PROFIT
FROM
	authors as au
    INNER JOIN titleauthor AS ta ON au.au_id = ta.au_id
    INNER JOIN titles AS t ON ta.title_id = t.title_id
    INNER JOIN sales AS s ON t.title_id = s.title_id
GROUP BY `AUTHOR ID`
ORDER BY PROFIT DESC
LIMIT 3;

-- This solution is valid if we suppose the royalty is independent from sales.
-- I tried something like this but did not work:

SELECT
	au.au_id AS `AUTHOR ID`,
    au.au_lname AS `LAST NAME`,
    au.au_fname AS `FIRST NAME`,
    SUM((s.qty*t.price + t.advance)*rs.royalty*ta.royaltyper) AS PROFIT
FROM
	authors as au
    INNER JOIN titleauthor AS ta ON au.au_id = ta.au_id
    INNER JOIN titles AS t ON ta.title_id = t.title_id
    INNER JOIN sales AS s ON t.title_id = s.title_id
    INNER JOIN (
		(SELECT 
			s.title_id,
			SUM(s.qty) AS total_sales
		FROM
			sales AS s
		GROUP BY s.title_id) AS totals
        INNER JOIN roysched AS rs ON totals.title_id = rs.title_id
			WHERE totals.total_sales >= rs.lorange AND total_sales < rs.hirange) AS roy ON s.title_id = roy.title_id 
GROUP BY `AUTHOR ID`
ORDER BY PROFIT DESC
LIMIT 3;
