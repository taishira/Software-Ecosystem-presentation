WITH CountryTags AS (
    SELECT 
        U.Location,
        T.TagName,
        COUNT(*) AS QuestionCount
    FROM Posts P
    INNER JOIN Users U ON P.OwnerUserId = U.Id
    INNER JOIN PostTags PT ON P.Id = PT.PostId
    INNER JOIN Tags T ON PT.TagId = T.Id
    WHERE 
        P.PostTypeId = 1 AND -- Questions
        U.Location IN ('United States', 'United Kingdom', 'Germany', 'India', 'Canada', 'France', 'Brazil', 'Australia', 'Netherlands', 'Russia') -- 例としての国リスト
    GROUP BY 
        U.Location, 
        T.TagName
),
RankedCountryTags AS (
    SELECT 
        Location,
        TagName,
        QuestionCount,
        ROW_NUMBER() OVER (PARTITION BY Location ORDER BY QuestionCount DESC) AS Rank
    FROM CountryTags
)
SELECT 
    Location, 
    TagName, 
    QuestionCount
FROM RankedCountryTags
WHERE Rank <= 10