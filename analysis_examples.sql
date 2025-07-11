
-- 이벤트별 카운트 분석
SELECT event_name, COUNT(*) AS event_count
FROM `your_project.analytics_123456789.events_*`
GROUP BY event_name
ORDER BY event_count DESC;
