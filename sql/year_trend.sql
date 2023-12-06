WITH TagCounts AS (
    SELECT 
        YEAR(Posts.CreationDate) AS Year,
        Tags.TagName,
        COUNT(*) AS NumberOfQuestions
    FROM Posts
    JOIN PostTags ON Posts.Id = PostTags.PostId
    JOIN Tags ON PostTags.TagId = Tags.Id
    WHERE 
        Posts.PostTypeId = 1 -- 1 is for Questions
    GROUP BY 
        YEAR(Posts.CreationDate),
        Tags.TagName
)
SELECT 
    Year,
    TagName,
    NumberOfQuestions
FROM (
    SELECT 
        Year,
        TagName,
        NumberOfQuestions,
        ROW_NUMBER() OVER(PARTITION BY Year ORDER BY NumberOfQuestions DESC) as Rank
    FROM TagCounts
) RankedTags
WHERE 
    Rank <= 10
ORDER BY 
    Year, 
    Rank