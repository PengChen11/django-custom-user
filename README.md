# Lab: Django Custom User

## Overview

Django does a great job at allowing to get started with a solid foundation. But a foundation is just the beginning. We still need to “build the house.”

One of the first things many developers need to do is have a custom user.

For this lab you’ll build your application from the very beginning with a Custom User model.

## Feature Tasks and Requirements

- create Django application from scratch that has a custom user model named CustomUser
- Custom user should use email instead of username for signup / login
- Application should work with Django Admin

## Implementation Notes

- Make sure to create custom user model before migrating data

## User Acceptance Tests

- Verify the creation of a new user with email and password
- Verify that duplicate emails are not allowed
