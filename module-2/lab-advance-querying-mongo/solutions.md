## Solutions
### Query #1
Filter: `{ "name": "Babelgum" }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd675297da0"
    },
...
```
### Query #2
Filter: `{ "number_of_employees": { $gt: 500 } }`

Sort: `{ "number_of_employees": 1 }`

Limit: 20

Output:
```
{
    "_id": {
        "$oid": "52cdef7d4bab8bd675299470"
    },
...
```
### Query #3
Filter: `{ $and: [ { founded_year: { $gte: 2000 } }, { founded_year: { $lte: 2005 } } ] }`

Porject: `{ name: 1, founded_year: 1 }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd675297d8c"
    },
...
```
### Query #4
Filter: `{ $and: [ { "ipo.valuation_amount": { $gt: 10e8} }, { founded_year: { $lt: 2010 } } ] }`

Project: `{ name: 1, ipo: 1 }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd675297d8e"
    },
...
```

### Query #5
Filter: `{ $and: [ { number_of_employees: { $lt: 1000} }, { founded_year: { $lt: 2005 } } ] }`

Sort: `{ number_of_employees: 1 }`

Limit: 10

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd675297e12"
    },
...
```
### Query #6
Filter: `{ $not: { partners: $exists } }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd675297d8b"
    },
...
```
### Query #7
Filter: `{ category_code: { $type: 10 } }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd6752980f6"

    },
...
```
### Query #8
Filter: `{ $and: [ { number_of_employees: { $gte: 100 } },  {number_of_employees: { $lt: 1000 } } ] }`

Projection: `{ name: 1, number_of_employees: 1 }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd675297d8b"

    },
...
```
### Query #9
Sort: `{ "ipo.valuation_amount": -1 }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7e4bab8bd67529a8b4"

    },
...
```
### Query #10
Sort: `{ number_of_employees: -1 }`

Limit: 10

Output:
```
{
    "_id": {
        "$oid": "52cdef7d4bab8bd67529941a"

    },
...
```
### Query #11
Sort: `{ founded_month: { $in: [7, 8, 9, 10, 11, 12] } }`

Limit: 100

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd675297d8c"

    },
...
```
### Query #12
Filter: `{ founded_year: { $lt: 2000 }, "acquisitions.price_amount": { $gt: 10e7 } }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7d4bab8bd67529941a"

    },
...
```
### Query #13
Filter `{ $and: [ { "acquisition.acquired_year": { $gt: 2010 } }, { acquisition: { $not: { $type: 10 } } } ] }`

Project: `{ name: 1, acquisition: 1 }`

Sort: `{ "acquisition.price_amount": -1  }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd675298876"

    },
...
```
### Query #14
Filter: `{ founded_year: { $not: { $type: 10 } } }`

Project: `{ name: 1, founded_year: 1 }`

Sort: `{ founded_year: 1 }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7e4bab8bd67529b1bc"

    },
...
```
### Query #15
Filter: `{ founded_day: { $lte: 7 } }`

Sort: `{ "acquisition.price_amount": -1 }`

Limit: 10

Output:
```
{
    "_id": {
        "$oid": "52cdef7d4bab8bd6752989a1"

    },
...
```
### Query #16
Filter: `{ $and: [ { category_code: "web" }, { number_of_employees: { $gt: 4000 } } ] }`

Sort: `{ number_of_employees: 1 }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd67529822a"

    },
...
```
### Query #17
Filter: `{ $and: [ { "acquisition.price_amount": { $gt: 10e7 } }, { "acquisition.price_currency_code": "EUR"} ] }`

Output:
```
{
    "_id": {
        "$oid": "52cdef7d4bab8bd675298bf3"

    },
...
```
### Query #18
Filter: `{ "acquisition.acquired_month": { $in: [1, 2, 3] } }`

Project: `{ name: 1, acquisition: 1 }` 

Limit: 10

Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd675297dab"

    },
...
```
### Query #19
Filter:
```
{ $and: [
    { founded_year: { $gte: 2000 } },
    { founded_year: { $lte: 2010 } },
    { 'acquisition.acquired_year': { $not: { $lt: 2011 } } }
  ]
}
```

Limit: 10
 
Output:
```
{
    "_id": {
        "$oid": "52cdef7c4bab8bd675297d8c"

    },
...
```