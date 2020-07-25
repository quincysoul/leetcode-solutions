# 8-stringToIntAtoi

- Seems the main purpose of the leetcode version is to handle large numbers of edge cases.
- I avoided using parseInt because that's basically the function you are trying to implement.
- The phrasing is a little bit confusing at some points
`00000` is allowed before a number and those zeros get ignored
`+` is allowed, which I didn't notice on my first try
` ` space character is supposed to break the parse if they have already started parsing a number. Didn't notice on first try.
- There are a lot of forum solutions which do not use hashmap for char to int conversion, but I think that's the most universal solution.
- I think taking it out of a for loop and into something like reduce would overcomplicate it.