# Thinkific Python SDK
This is a Python SDK to interact with the
[Thinkific LMS](http://www.thinkific.com/) API. The official documentation for the API can be found
[here](https://api.thinkific.com/documentation).
## Usage
### Initialize

1) Import the library
  ``` python
  from thinkific import Thinkific 
  ```
2) Create an object with the Auth token and subdomain name
  ``` python
  thinkific = Thinkific("<auth_token>","<subdomain>")
  ```

### Endpoints
The following endpoints are currently supported:
- Bundles
- Chapters
- Contents
- Coupons
- Course reviews (course_reviews)
- Courses
- Enrollments
- Orders
- Products
- Promotions
- Users

Each endpoint can be initialized in the following way:
``` python
  users= thinkific.users
  courses=thinkific.courses
  ```
### Methods
The methods can be accessed as below
``` python
  thinkific = Thinkific("<auth_token>","<subdomain>")
  thinkific.courses.list()
  ```
The python methods corresponding to each API contents will be listed below:
#### Bundles
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve A Bundle</td>
    <td class="tg-yw4l">retrieve_bundle()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve the Courses Within A Bundle</td>
    <td class="tg-yw4l">retrieve_courses_in_bundle()</td>
  </tr>
   <tr>
    <td class="tg-yw4l">Create an Enrollment in a Bundle of Courses</td>
    <td class="tg-yw4l">create_enrollment_in_bundle()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Get Enrollments in a Bundle</td>
    <td class="tg-yw4l">get_enrollments_in_bundle()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Update Enrollments in a Bundle</td>
    <td class="tg-yw4l">update_enrollments_in_bundle()</td>
  </tr>
</table>

#### Chapters
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve A Chapter</td>
    <td class="tg-yw4l">retrieve_chapter()</td>
  </tr>
  
  <tr>
    <td class="tg-yw4l">Retrieve the Contents of a Chapter</td>
    <td class="tg-yw4l">retrieve_contents_of_chapter()</td>
  </tr>
</table>

#### Contents
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve A Content</td>
    <td class="tg-yw4l">retrieve_content()</td>
  </tr>
</table>

#### Coupons
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a list of Coupons</td>
    <td class="tg-yw4l">list()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a Coupon</td>
    <td class="tg-yw4l">retrieve_coupon()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Create a Coupon</td>
    <td class="tg-yw4l">create_coupon()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Bulk Create Coupons</td>
    <td class="tg-yw4l">bulk_create_coupons()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Update a Coupon</td>
    <td class="tg-yw4l">update_coupon()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Delete a Coupon</td>
    <td class="tg-yw4l">delete_coupon()</td>
  </tr>
</table>

#### Course Reviews
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a list of Reviews for a Course</td>
    <td class="tg-yw4l">list()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Create a Course Review</td>
    <td class="tg-yw4l">create_course_review()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a Course Review</td>
    <td class="tg-yw4l">retrieve_course_review()</td>
  </tr>
</table>

#### Courses
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a list of Courses</td>
    <td class="tg-yw4l">list()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a Course</td>
    <td class="tg-yw4l">retrieve_course()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve the Chapters of a Course</td>
    <td class="tg-yw4l">retrieve_chapters()</td>
  </tr>
</table>

#### Enrollments
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a list of Enrollments</td>
    <td class="tg-yw4l">list()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve an Enrollment</td>
    <td class="tg-yw4l">retrieve_enrollment()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Create an Enrollment</td>
    <td class="tg-yw4l">create_enrollment()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Update an Enrollment</td>
    <td class="tg-yw4l">update_enrollment()</td>
  </tr>
</table>

#### Orders
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a list of Orders</td>
    <td class="tg-yw4l">list()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve an Order</td>
    <td class="tg-yw4l">retrieve_order()</td>
  </tr>
</table>

#### Products
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a list of Products</td>
    <td class="tg-yw4l">list()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a Product</td>
    <td class="tg-yw4l">retrieve_product()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a list of Products related to another Product</td>
    <td class="tg-yw4l">retrieve_product_related()</td>
  </tr>
</table>

#### Promotions
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a list of Promotions</td>
    <td class="tg-yw4l">list()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a Promotion</td>
    <td class="tg-yw4l">retrieve_promotion()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Create a Promotion</td>
    <td class="tg-yw4l">create_promotion()</td>
  </tr>
   <tr>
    <td class="tg-yw4l">Update a Promotion</td>
    <td class="tg-yw4l">update_promotion()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Delete a Promotion</td>
    <td class="tg-yw4l">delete_promotion()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Find a Promotion by Coupon Code and Product</td>
    <td class="tg-yw4l">find_promotion_with_coupon_and_product()</td>
  </tr>
</table>

#### Users
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Content</b></th>
    <th class="tg-yw4l"><b>Function</b></th>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a list of Users</td>
    <td class="tg-yw4l">list()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Retrieve a User</td>
    <td class="tg-yw4l">retrieve_user()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Create a User</td>
    <td class="tg-yw4l">create_user()</td>
  </tr>
   <tr>
    <td class="tg-yw4l">Update a User</td>
    <td class="tg-yw4l">update_user()</td>
  </tr>
  <tr>
    <td class="tg-yw4l">Delete a User</td>
    <td class="tg-yw4l">delete_user()</td>
  </tr>
</table>

For more details, please look at the [Thinkific API Docs](https://api.thinkific.com/documentation).

TODO:
- Add the remaining API endpoints
