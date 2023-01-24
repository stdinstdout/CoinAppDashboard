SELECT SUBSTR(issue_key, 1, 1) AS task_group,
    ROUND(AVG(minutes_in_status / 60), 2) as "avg_opened_time"
FROM history
WHERE history.status = 'Open'
GROUP BY task_group;