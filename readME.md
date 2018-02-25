# Name Dupliaction Problem

Variation in names leads to difficulty in identifying a unique person and hence deduplication of records is an unsolved challenge. The problem becomes more complicated in cases where data is coming from multiple sources. Following variations are same as Vladimir Frometa:

Vladimir Antonio Frometa Garo
Vladimir A Frometa Garo
Vladimir Frometa
Vladimir Frometa G
Vladimir A Frometa Vladimir A Frometa G

This model is trained to reduce duplication of records with various formats of names.

It uses Decision Trees and classification to filter out unique users from the records with their first names, and then it makes the decision further on with other features.
The unique record list will be saved in another file called Records.

<h6>Run-time: Python 3<h6>
<h6>Dependencis: Pandas </h6>


