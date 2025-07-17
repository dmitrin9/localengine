# localengine

For situations where you're traveling without service or wifi such as on an airplane,  
put directories containing HTML documents into localengine `search/` directory and run the  
server locally to search them.

---

## Usage

* Put directory containing HTML into `serach/`

* When searching, use the route `/search/<terms>` where terms are divided by plus signs. Example: `/search/hello+world`

---

## Notes

Firefox doesn't let you link to file URIs in anchors for security reasons, so the URI is shown but not linked.  
I'll probably fix this later. I'm currently without wifi so I can't exactly google the answer.
