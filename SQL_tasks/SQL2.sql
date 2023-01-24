SELECT issue_key,
    status,
    DATETIME(ROUND(MAX(started_at) / 1000), 'unixepoch') as "started_datetime"
FROM history
GROUP BY issue_key
HAVING "started_datetime" BETWEEN DATE('2019-06-03') AND DATE('2023-01-10')
    AND status != 'Closed'
    AND status != 'Resolved';