<div id="beginning">

# REST
</div>

![REST API](img/api-rest.png)

<b>Table Of Contents</b> |
------------ | 
[Introduction - What is an API?](#api)
[REST Architecture](#rest-arch)
[REST APIs and Web Services](#rest-http)
[REST and Python — Requests Library](#rest-python-requests)
[REST and Python — Building APIs](#rest-python-building-apis)
<!-- [REST and Python — Tools and Frameworks](#rest-python-tools-frameworks)
[Building REST APIs using Flask and Python](#apis-using-flask-and-python)
-->

<div id="api">
<h2>Introduction - What is an API?</h2>
<p>The term API stands for "Application Programming Interface". Imagine a cook-for-yourself restaurant, where you can prepare your own dish and the ingredients are provided to you if you wish. You can also bring your own ingredients in and ask them for a ready dish! The menu of ingredients in this restaurant would be the API. When you specify what menu items you want, the restaurant's freezer has them ready for you and if the item you ask for is a ready dish, you don't know exactly how the restaurant prepares it, and you don't really need to.</p>

<p>Similarly, an API lists a bunch of operations that developers can use, along with a documentation(description) of their purpose. The developers just need to know that it is available for use in their app. They can provide own data to the API to get the results. </p>

<p>APIs make life easier for developers by providing reusable and distributable code. For example, if you are willing to make an app for iOS where you'd process the image taken by the iPhone's camera, you don't have to write your own camera interface. Instead, you can use the camera API to embed the iPhone's built-in camera in your app. If APIs didn’t exist to make this easy, app developers would have to create their own camera software and interpret the camera hardware’s inputs. But Apple’s operating system developers have done all this hard work so the developers can just use the camera API to embed a camera, and then get on with building their app. And, when Apple improves the camera API, all the apps that rely on it will take advantage of that improvement automatically. </p>

<p>This applies to every platform. For example, do you want to create a dialog box on Windows? There’s an API for that. Want to support fingerprint authentication on Android? There’s an API for that, too, so you don’t have to test every different Android manufacturer’s fingerprint sensor. Developers don’t have to reinvent the wheel over and over.</p>

<p><strong>In short, the API mediates between applications via requests and responses.</strong> For instance, registration in the application through the user's existing Twitter account occurs through the Twitter API that developers have integrated into the app.</p>

![API Timeline](img/api-rest-timeline.png)

The API uses various protocols and architectures for sending requests and responses:
<ul>
<li> <strong>XML-RPC</strong> — allows the exchange of functions between networks. XML-RPC uses XML to describe responses/requests and HTTP protocols for information transferring from client to server.</li>
<li><strong>JSON-RPC</strong> is a lightweight RPC similar to XML. Here protocol is encoded in JSON; it allows receiving calls to the server with asynchronous responses.</li>
<li><strong>SOAP</strong> — a simple object access protocol for exchanging structured information when implementing web services in computer networks. SOAP uses XML for authentication, authorization, and process communication on operating systems. It allows clients to call web services and receive responses regardless of platform and language.</li>
<li><strong>REST API (representative state transfer)</strong> — an architectural style using client-server implementations independently. REST uses HTTP protocol for communication.</li>
</ul>
</div>

<div id="rest-arch">
<h2>REST Architecture</h2>
<strong>REST</strong> stands for <strong>re</strong>presentational <strong>s</strong>tate <strong>t</strong>ransfer and is a software architecture style that defines a pattern for client and server communications over a network. REST provides a set of constraints for software architecture to promote performance, scalability, simplicity and reliability in the system.

REST defines the following architectural constraints:
<ul>
    <li><strong>Stateless:</strong> The server won't maintain any state between requests from the client and won't contain any data about the client. All information needed for request processing is included in the request. The client stores all session information.</li>
    <li><strong>Client-server:</strong> The REST API implements a client-server architecture style. 
    <ul>
    <li>The client is sending requests for resources and is not associated with the data storage.</li>
    <li>Data storage remains inside the server.</li>
    <li>Servers are not involved in the communication with the user interface.</li>
    <li>The client and server evolve interdependently.</li></ul> This factor makes the REST even more flexible and scalable.</li>
    <li><strong>Cacheable:</strong> The data retrieved from the server should be cacheable either by the client or by the server. If the data is cacheable, then in similar requests, the client can use the same data without repeatedly sending requests to the server. It helps improve performance and availability.</li>
<li><strong>Uniform interface:</strong> The unified interface is an essential factor distinguishing the REST API. It states that there is a single way for communicating with the server, not implying the type of application and device.
    <ul>
    <li><i>Identification of resources.</i> Each resource must have an identification that is independent of the resource's state. The <strong>URL</strong> acts as an identifier.</li>
    <li><i>Manipulation of resources through representations.</i> A resource representation (that client has) contains the data required to delete or modify the resource. The client sends a representation (a JSON object) that the server needs to modify, remove, or add.</li>
    <li><i>Self descriptive messages.</i> Each message has enough information for the server to parse the request. No additional information is required in separate documentation or messages.</li>
    <li><i>Hypermedia as the engine of application state.</i> Hypermedia requires links usage for each response so that the client can find other resources. In REST, hypermedia is used for all interactions.</li>
    </ul>
</li>
<li><strong>Layered system:</strong> The client may access the resources on the server indirectly through other layers such as a proxy or load balancer.</li>
<li><strong>Code on demand(optional):</strong> The server may transfer code to the client that it can download and run.</li>
</ul>
<strong>REST is not a specification but a set of guidelines on how to architect a network-connected software system.</strong>
</div>

<div id="rest-http">
<h2>REST APIs and Web Services</h2>

![REST Model](img/api-rest-model.png)
<p>A REST web service is any web service that adheres to REST architecture constraints. These web services expose their data to the outside world through an API. REST APIs provide access to web service data through public web URLs.</p>

For example, here's one of the URLs for GitHub's REST API:

```http
https://api.github.com/users/<username>
https://api.github.com/users/AxoyTO
```
This URL allows to access information about a specific GH user. We access data from a REST API by sending HTTP request to a specific url and processing the response.

<h3>HTTP Requests</h3>
<p>REST API communicates through HTTP requests. A <strong>resource</strong> is any data available in the web service that can be accessed and manipulated with <strong>HTTP</strong> requests to the REST API. The HTTP method tells the API which action to perform on the resource.</p>

<p align="center"><img src="img/api-rest-methods-detail.jpeg" alt="HTTP Methods" width="400"></p>

<h3>Status Codes</h3>
<p>Once a REST API receives and processes an HTTP request, it will return an HTTP response. Included in this response is an HTTP status code. This code provides information about the results of the request. An application sending requests to the API can check the status code and perform actions based on the result. These actions could include handling errors or displaying a success message to a user.</p>
<p align="center"><img src="img/status-codes.jpeg" alt="HTTP Status Codes" width="400"></p>

Most common status codes returned by REST APIs:
<table>
    <tr>
        <th>Code</th>
        <th>Meaning</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>200</td>
        <td>OK</td>
        <td>The requested action was successful.</td>
    </tr>
    <tr>
        <td>201</td>
        <td>Created</td>
        <td>A new resource was created.</td>
        </tr>
    <tr>
        <td>202</td>
        <td>Accepted</td>
        <td>The request was received, but no modification has been made yet.</td>
    </tr>
    <tr>
        <td>204</td>
        <td>No Content</td>
        <td>The request was successful, but the response has no content.</td>
    </tr>
    <tr>
        <td>400</td>
        <td>Bad Request</td>
        <td>The request was malformed.</td>
    </tr>
    <tr>
        <td>401</td>
        <td>Unauthorized</td>
        <td>The client is not authorized to perform the requested action.</td>
    </tr>
    <tr>
        <td>404</td>
        <td>Not Found</td>
        <td>The requested resource was not found.</td>
    </tr>
    <tr>
        <td>415</td>
        <td>Unsupported Media Type</td>
        <td>The request data format is not supported by the server.</td>
    </tr>
    <tr>
        <td>422</td>
        <td>Unprocessable Entity</td>
        <td>The request data was properly formatted but contained invalid or missing data.</td>
    </tr>
    <tr>
        <td>500</td>
        <td>Internal Server Error</td>
        <td>The server threw an error when processing the request.</td>
    </tr>
    
</table>
</div>

<div id="rest-python-requests">
<h2>REST and Python — Requests Library</h2>

<p align="center" width="50%"><img src="img/requests-lib-logo.png" alt="Requests Library Logo" width="300"></p>
<p>The <strong>requests</strong> library abstracts away the complexities of making HTTP requests.

To start using <strong>requests</strong>, we need to install it first. We can use python package installer(pip) to install it:</p>
```sh
python -m pip install requests
```
<h3>GET</h3>
<p><strong>GET</strong> is one of the most common HTTP methods we'll use when working with REST APIs. <strong>GET</strong> allows us to retrieve resources from a given API. <strong>GET</strong> is a <strong>read-only</strong> operation.</p>

```py
import requests
api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true"
response = requests.get(api_url)
print(response.ok) # True
print(response.status_code) # 200
print(response.request) # <PreparedRequest [GET]>
print(response.url) # 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true'
print(response.json()) 
# {'bitcoin': {'usd': 20094, 'usd_24h_change': -2.7382059716452076}}
```

<h3>POST</h3>
<p>CoinGecko doesn't have a free POST API. Thus, we'll use a service called JSONPlaceholder, which provides fake API endpoints that send back responses that <strong>requests</strong> can process. Here's the data we'll send:</p>

```json
{
    "userId": 1,
    "title": "Buy milk",
    "completed": false
}
```

<p>This JSON contains information for a new <u>todo</u> item. We run the following code to create a <u>todo</u>:</p>

```py
import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.json()) # {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}
print(response.status_code) # 201
```
<p>Unless we want simplicity, we can do this in a more complex way without using the <i>json</i> keyword. We would've needed to set <i>Content Type</i> accordingly and serialize the JSON manually with the help of JSON library.</p>
```py
import requests, json
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers = {"Content Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
print(response.json()) 
# {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}
print(response.status_code) # 201
```
<p>The <i>headers</i> dictionary that contains a single header <i>Content-Type</i> set to <>application/json</i> tells the REST API that we're sending JSON data with the POST request.</p>

<h3>PUT</h3>
<p>Beyond <strong>GET</strong> and <strong>POST</strong>, requests provides support for all the other HTTP methods we would use with a REST API. The following code sends a PUT request to update an existing <u>todo</u> with new data. Any data sent with a <strong>PUT</strong> request will completely replace the existing values of the <u>todo</u>.</p>

```py
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())
# {'userId': 1, 'id': 10, 'title': 'illo est ... aut', 'completed': True}

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())
# {'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}

print(response.status_code) # 200
```
<p>Note that successful <strong>PUT</strong> requests will always return 200 instead of 201 because we aren't creating a new resource but just updating an existing one.</p>

<h2>PATCH</h2>
<p>We will use <strong>PATCH</strong> to modify the value of a specific field on an existing <u>todo</u>. <strong>PATCH</strong> differs from <strong>PUT</strong> in that it doesn’t completely replace the existing resource. It only modifies the values set in the JSON sent with the request.</p>

```py
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Study for the exams"}
response = requests.patch(api_url, json=todo)
print(response.json())
# {'userId': 1, 'id': 10, 'title': 'Mow lawn', 'completed': True}

print(response.status_code) # 200
```

<h2>DELETE</h2>
<p>If we want to completely remove a resource, then we use DELETE. Here’s the code to remove a <u>todo</u>:</p>

```py
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json()) # {}
print(response.status_code) # 200
```
<p>The API URL contains the id of the <u>todo</u> we would like to remove. This sends a <strong>DELETE</strong> request to the REST API, which then removes the matching(by id) resource.</p>


</div>

<div id="rest-python-building-apis">
<h2>REST and Python — Building APIs</h2>
<p>The first step we take as we build a REST API is to identify the resources, e.g. <i>customers, events, transactions</i>, the API will manage. We should also consider the nested resources. For example, a customer may have <i>sales</i> or events may contain <i>guests</i>. Establishing these resource hierarchies will help when we define API endpoints.
</p>

<h3>Defining Endpoints</h3>
<p>Once we've identified the resources in our web service, we'll want to use these to define the API endpoints. Here is an example of `transactions` endpoint we might find in an API for a payment processing service.</p>
<table>
    <tr>
        <th>HTTP Method</th>
        <th>API Endpoint</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>GET</td>
        <td>/transactions</td>
        <td>Get a list of transactions</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/transactions/&lttransaction_id&gt</td>
        <td>Get a single transaction</td>
    </tr>
    <tr>
        <td>POST</td>
        <td>/transactions</td>
        <td>Create a new transaction</td>
    </tr>
    <tr>
        <td>PUT</td>
        <td>/transactions/&lttransaction_id&gt</td>
        <td>Update a transaction</td>
    </tr>
    <tr>
        <td>PATCH</td>
        <td>/transactions/&lttransaction_id&gt</td>
        <td>Partially update a transaction</td>
    </tr>
    <tr>
        <td>DELETE</td>
        <td>/transactions/&lttransaction_id&gt</td>
        <td>Delete a transaction</td>
    </tr>
</table>
<p>These endpoints cover all the <strong>CRUD(Create-Read-Update-Delete)</strong> operations</p>

<p><strong>Note:</strong> An endpoint shouldn't contain verbs. for example, the endpoint below contains an unneeded verb:</p>

```http
GET /getTransactions
```
Instead, we should have a proper endpoint name, which won't confuse us when we want to interact using any(almost) of the HTTP Methods.
```http
GET /transactions
```

Now, let's take a look at an example of endpoints for a nested resource:
<table>
    <tr>
        <th>HTTP Method</th>
        <th>API Endpoint</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>GET</td>
        <td>/events/&ltevent_id&gt/guests</td>
        <td>Get a list of guests</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/events/&ltevent_id&gt/guests/&ltguest_id&gt</td>
        <td>Get a single guest</td>
    </tr>
    <tr>
        <td>POST</td>
        <td>/events/&ltevent_id&gt/guests</td>
        <td>Create a new guest</td>
    </tr>
    <tr>
        <td>PUT</td>
        <td>/events/&ltevent_id&gt/guests/&ltguest_id&gt</td>
        <td>Update a guest</td>
    </tr>
    <tr>
        <td>PATCH</td>
        <td>/events/&ltevent_id&gt/guests/&ltguest_id&gt</td>
        <td>Partially update a guest</td>
    </tr>
    <tr>
        <td>DELETE</td>
        <td>/events/&ltevent_id&gt/guests/&ltguest_id&gt</td>
        <td>Delete a guest</td>
    </tr>
</table>

<p>This is not the only way to define an endpoint for nested resources. There is also another option called <strong>query strings</strong> to access a nested resource. A query string allows you to send additional parameters with your HTTP request. In the following endpoint, we append a query string to get <i>guests</i> for a specific <i>event_id</i>:</p>

```HTTP
GET /guests?event_id=23
```

<strong>Note:</strong> REST API, with any other technology, keeps evolving and it's always expected to change throughout the life of a web service. Resources will change, and endpoints need to be updated to reflect these changes. This is where <strong>API versioning</strong> comes in. API versioning allows us to modify our API without fear of breaking existing integrations.


<h3>API Versioning</h3>
<h4>URI Versioning</h4>
<p>Each time we modify the web API or change the schema of resources, we add a version number to the URI for each resource. For example, if there has been an <i>address</i> field and it has been restructured into subfields such as <i>streetAddress, city, state, zipCode</i>, this version of the resource could be exposed through a URI containing a version number, such as 

```HTTP
https://retailer.com/v2/customers/3
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"id":3,"name":"Sec Cars","dateCreated":"2014-09-04T12:11:38","address":{"streetAddress":"Yaroslovskoe Shosse","city":"Moscow","state":"Moscow Oblast","zipCode":129337}}
```

<p>This versioning mechanism is very simple but depends on the server routing the request to the appropriate endpoint. However, it can become unwieldy as the web API matures through several iterations and the server has to support a number of different versions. Also, from a purist's point of view, in all cases the client applications are fetching the same data (customer 3), so the URI should not really be different depending on the version.</p>

<h4>Query String Versioning</h4>
<p>Rather than providing multiple URIs, we can specify the version of the resource by using a parameter within the query string appended to the HTTP request, such as:

```HTTP
https://retailer.com/customers/3?version=2
```

The version parameter should default to a meaningful value such as 1 if it is omitted by older client applications. This approach has the semantic advantage that the same resource is always retrieved from the same URI, but it depends on the code that handles the request to parse the query string and send back the appropriate HTTP response.

<strong>Note:</strong> Some older web browsers and web proxies does not cache responses for requests that include a query string in the URI. This can degrade performance for web applications that use a web API and that run from within such a web browser.</p>

<h4>Header Versioning</h4>
<p>Rather than appending the version number as a query string parameter, we could implement a custom header that indicates the version of the resource. This approach requires that the client application adds the appropriate header to any requests, although the code handling the client request could use a default value (version 1) if the version header is omitted. The following examples use a custom header named Custom-Header. The value of this header indicates the version of web API.</p>

<h5>Version 1:</h5>
```http
GET https://retailer.com/customers/3 HTTP/1.1
Custom-Header: api-version=1
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"id":3,"name":"Sec Cars","address":"Yaroslovskoe Shosse Moscow Moscow Oblast 129337}
```
<h5>Version 2:</h5>

```http
GET https://retailer.com/customers/3 HTTP/1.1
Custom-Header: api-version=2

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"id":3,"name":"Sec Cars","dateCreated":"2014-09-04T12:11:38","address":{"streetAddress":"Yaroslovskoe Shosse","city":"Moscow","state":"Moscow Oblast","zipCode":129337}}
```

<p><strong>Note:</strong> No matter which versioning strategy we use, versioning our API is an important step to ensure it can adapt to changing requirements while supporting existing resources.</p>


<h3>Data Interchange Format</h3>
<p>Two popular options for formatting web service data are XML and JSON. Traditionally, XML was very popular with SOAP APIs, but JSON is more popular with REST APIs. To compare the two, take a look at an example book resource formatted as XML and JSON.

Here’s the book formatted as XML:</p>
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<book>
    <title>Python Basics</title>
    <page_count>635</page_count>
    <pub_date>2021-03-16</pub_date>
    <authors>
        <author>
            <name>David Amos</name>
        </author>
        <author>
            <name>Joanna Jablonski</name>
        </author>
        <author>
            <name>Dan Bader</name>
        </author>
        <author>
            <name>Fletcher Heisler</name>
        </author>
    </authors>
    <isbn13>978-1775093329</isbn13>
    <genre>Education</genre>
</book>
```
<p>XML uses a series of elements to encode data. Each element has an opening and closing tag, with the data in between. Elements can be nested inside other elements. We can see this above, where several &ltauthor&gt tags are nested inside of &ltauthors&gt.

Now, take a look at the same book in JSON:</p>

```json
{
    "title": "Python Basics",
    "page_count": 635,
    "pub_date": "2021-03-16",
    "authors": [
        {"name": "David Amos"},
        {"name": "Joanna Jablonski"},
        {"name": "Dan Bader"},
        {"name": "Fletcher Heisler"}
    ],
    "isbn13": "978-1775093329",
    "genre": "Education"
}

```

<p>JSON stores data in key-value pairs similar to a Python dictionary. Like XML, JSON supports nesting data to any level, so we can model complex data.</p>


<h3>Design Success Responses</h3>
<p>Once we’ve picked a data format, the next step is to decide how we’ll respond to HTTP requests. All responses from our REST API should have a similar format and include the proper HTTP status code.

Now we’ll look at some example HTTP responses for a hypothetical API that manages an inventory of cars. To make things clear, we’ll look at raw HTTP requests and responses instead of using an HTTP library like requests.

To start things off, we'll take a look at a GET request to /cars, which returns a list of cars:</p>

```http
GET /cars HTTP/1.1
Host: api.example.com
```

<p>This HTTP request is made up of four parts:</p>
<ol>
<li>GET is the HTTP method type.</li>
<li>/cars is the API endpoint.</li>
<li>HTTP/1.1 is the HTTP version.</li>
<li>Host: api.example.com is the API host.</li>
</ol>

<p>These four parts are all we need to send a GET request to /cars. Now let's take a look at the response. This API uses JSON as the data interchange format:</p>

```http
HTTP/1.1 200 OK
Content-Type: application/json
...

[
    {
        "id": 1,
        "make": "GMC",
        "model": "1500 Club Coupe",
        "year": 1998,
        "vin": "1D7RV1GTXAS806941",
        "color": "Red"
    },
    {
        "id": 2,
        "make": "Lamborghini",
        "model":"Gallardo",
        "year":2006,
        "vin":"JN1BY1PR0FM736887",
        "color":"Mauve"
    },
    {
        "id": 3,
        "make": "Chevrolet",
        "model":"Monte Carlo",
        "year":1996,
        "vin":"1G4HP54K714224234",
        "color":"Violet"
    }
]
```

<p>When we are working with a real API, we are going to see more HTTP headers than this. These headers differ between APIs.

It’s important to always set the correct <i>Content-Type</i> header on our response. If we send JSON, then we set Content-Type to application/json. If XML, then set it to application/xml. This header tells the user how they should parse the data.

For any successful GET request, we should return 200 OK. This tells the user that their request was processed as expected.


Let's take a look at another GET request, this time for a single car:</p>

```http
GET /cars/1 HTTP/1.1
Host: api.example.com
```
This HTTP request queries the API for car 1. Here’s the response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 1,
    "make": "GMC",
    "model": "1500 Club Coupe",
    "year": 1998,
    "vin": "1D7RV1GTXAS806941",
    "color": "Red"
},
```
<p>This response contains a single JSON object with the car’s data. Since it’s a single object, it doesn’t need to be wrapped in a list. Like the last response, this also has a 200 OK status code.

<strong>Note:</strong>A GET request should never modify an existing resource. If the request contains data, then this data should be ignored and the API should return the resource unchanged.

Next up, let's check out a POST request to add a new car:</p>

```http
POST /cars HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "make": "Nissan",
    "model": "240SX",
    "year": 1994,
    "vin": "1N6AD0CU5AC961553",
    "color": "Violet"
}
```

<p>This POST request includes JSON for the new car in the request. It sets the Content-Type header to application/json so the API knows the content type of the request. The API will create a new car from the JSON.

Here’s the response:</p>
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 4,
    "make": "Nissan",
    "model": "240SX",
    "year": 1994,
    "vin": "1N6AD0CU5AC961553",
    "color": "Violet"
}
```
<p>This response has a <strong>201 Created</strong> status code to tell the user that a new resource was created. We need to make sure to use 201 Created instead of 200 OK for all successful POST requests.

This response also includes a copy of the new car with an id generated by the API. It’s important to send back an id in the response so that the user can modify the resource again.

Note: It’s important to always send back a copy of a resource when a user creates it with POST or modifies it with PUT or PATCH. This way, the user can see the changes that they’ve made.

Now let's take a look at a PUT request:</p>

```http
PUT /cars/4 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "make": "Buick",
    "model": "Lucerne",
    "year": 2006,
    "vin": "4T1BF3EK8AU335094",
    "color":"Maroon"
}
```
<p>This request uses the id from the previous request to update the car with all new data. As a reminder, PUT updates all fields on the resource with new data. Here’s the response:</p>

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 4,
    "make": "Buick",
    "model": "Lucerne",
    "year": 2006,
    "vin": "4T1BF3EK8AU335094",
    "color":"Maroon"
}
```

<p>The response includes a copy of the car with the new data. Again, we always want to send back the full resource for a PUT request. The same applies to a PATCH request:</p>

```http
PATCH /cars/4 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "vin": "VNKKTUD32FA050307",
    "color": "Green"
}
```

<p>PATCH requests only update a part of a resource. In the request above, the vin and color fields will be updated with new values. Here’s the response:</p>

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 4,
    "make": "Buick",
    "model": "Lucerne",
    "year": 2006,
    "vin": "VNKKTUD32FA050307",
    "color": "Green"
}
```

<p>The response contains a full copy of the car. As we can see, only the vin and color fields have been updated.

Finally, let's take a look at how our REST API should respond when it receives a DELETE request. Here’s a DELETE request to remove a car:</p>

```http
DELETE /cars/4 HTTP/1.1
```
<p>This DELETE request tells the API to remove the car with the ID 4. Here’s the response:</p>

```http
HTTP/1.1 204 No Content
```

<p>This response only includes the status code <strong>204 No Content</strong>. This status code tells a user that the operation was successful, but no content was returned in the response. This makes sense since the car has been deleted. There’s no reason to send a copy of it back in the response.</p>

<h3>Designing Error Responses</h3>
<p>There’s always a chance that requests to your REST API could fail. It’s a good idea to define what an error response will look like. These responses should include a description of what error occurred along with the appropriate status code.

To start, let's take a look at a request for a resource that doesn’t exist in the API:</p>

```http
GET /motorcycles HTTP/1.1
Host: api.example.com
```

<p>Here, the user sends a GET request to /motorcycles, which doesn’t exist. The API sends back the following response:</p>

```http
HTTP/1.1 404 Not Found
Content-Type: application/json
...

{
    "error": "The requested resource was not found."
}
```

<p>This response includes a <strong>404 Not Found</strong> status code. Along with this, the response contains a JSON object with a descriptive error message. Providing a descriptive error message gives the user more context for the error.

Now let's take a look at the error response when the user sends an invalid request:</p>

```http
POST /cars HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "make": "Nissan",
    "year": 1994,
    "color": "Violet"
```

<p>This POST request contains JSON, but it isn’t formatted correctly. It’s missing a closing curly brace (}) at the end. The API won’t be able to process this data. The error response tells the user about the issue:</p>

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "error": "This request was not properly formatted. Please send again."
}
```

<p>This response includes a descriptive error message along with the <strong>400 Bad Request</strong> status code, telling the user they need to fix the request.

There are several other ways that the request can be wrong even if it’s formatted properly. In this next example, the user sends a POST request but includes an unsupported media type:</p>

```http
POST /cars HTTP/1.1
Host: api.example.com
Content-Type: application/xml

<?xml version="1.0" encoding="UTF-8" ?>
<car>
    <make>Nissan</make>
    <model>240SX</model>
    <year>1994</year>
    <vin>1N6AD0CU5AC961553</vin>
    <color>Violet</color>
</car>
```
<p>In this request, the user sends XML, but the API only supports JSON. The API responds with this:</p>

```http
HTTP/1.1 415 Unsupported Media Type
Content-Type: application/json

{
    "error": "The application/xml mediatype is not supported."
}
```

In this next example, the user sends a POST request but includes car data that doesn’t match fields of the other data:

```http
POST /cars HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "make": "Nissan",
    "model": "240SX",
    "topSpeed": 120
    "warrantyLength": 10
}
```
<p>In this request, the user adds <i>topSpeed</i> and <i>warrantyLength</i> fields to the JSON. These fields aren’t supported by the API, so it responds with an error message:</p>

```http
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "error": "Request had invalid or missing data."
}
```

<p>This response includes the <strong>422 Unprocessable Entity</strong> status code. This status code indicates that there weren’t any issues with the request, but the data was invalid. A REST API needs to validate incoming data. If the user sends data with the request, then the API should validate the data and inform the user of any errors.</p>

</div>

<!-- <div id="rest-python-tools-frameworks">
<h2>REST and Python — Tools and Frameworks</h2>
</div>

<div id="apis-using-flask-and-python">
<h2>Building REST APIs using Flask and Python</h2>
</div>
-->
---

## References:

[AppMaster](https://appmaster.io/blog/what-rest-api-and-how-it-differs-other-types)

[RealPython](https://realpython.com/api-integration-in-python/#rest-architecture)

[Towards Data Science](https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24)

[HowToGeek](https://www.howtogeek.com/343877/what-is-an-api/)

[Microsoft Docs](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design)

<hr>

[Go to the beginning of the page](#beginning)