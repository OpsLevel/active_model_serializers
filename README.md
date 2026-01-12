# ActiveModelSerializers

## About

ActiveModel::Serializers provides a conventions-based approach to serializing resources in a Rails application. It allows you to generate JSON in an object-oriented and convention-driven manner, making it easier to build and maintain JSON APIs.

ActiveModelSerializers is undergoing some renovations. See [Development Status](#status-of-ams).

## Prerequisites

- **Ruby**: Version 2.1 or higher
- **Rails**: Compatible with Rails 4.x and 5.x (see [version compatibility](#documentation) for details)

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'active_model_serializers'
```

And then execute:

```bash
$ bundle install
```

Or install it yourself as:

```bash
$ gem install active_model_serializers
```

## Quick Start

### Basic Usage

Once installed, you can generate a serializer for your model:

```bash
$ rails generate serializer user
```

This creates a serializer file in `app/serializers/user_serializer.rb`:

```ruby
class UserSerializer < ActiveModel::Serializer
  attributes :id, :name, :email
end
```

### Using Serializers in Controllers

In your controller, Rails will automatically use the serializer:

```ruby
class UsersController < ApplicationController
  def show
    @user = User.find(params[:id])
    render json: @user
  end
end
```

### Customizing Serializers

You can customize your serializers by adding associations and custom attributes:

```ruby
class UserSerializer < ActiveModel::Serializer
  attributes :id, :name, :email, :full_name
  
  has_many :posts
  has_one :profile
  
  def full_name
    "#{object.first_name} #{object.last_name}"
  end
end
```

For more detailed usage examples and advanced features, please refer to the [Documentation](#documentation) section.

## Getting Help

If you find a bug, please report an [Issue](https://github.com/rails-api/active_model_serializers/issues/new)
and see our [contributing guide](CONTRIBUTING.md).

If you have a question, please [post to Stack Overflow](http://stackoverflow.com/questions/tagged/active-model-serializers).

If you'd like to chat, we have a [community slack](http://amserializers.herokuapp.com).

Thanks!

## Documentation

If you're reading this at https://github.com/rails-api/active_model_serializers you are
reading documentation for our `master`, which is not yet released.

<table>
  <tr>  
    <td>
      <a href='https://github.com/rails-api/active_model_serializers/tree/0-10-stable'>0.10 (0-10-stable) Documentation
      </a>
    </td>
    <td>
      <a href='http://www.rubydoc.info/gems/active_model_serializers/0.10.6'>
        <img src='http://img.shields.io/badge/yard-docs-blue.svg' />
      </a>
    </td>
    <td>
      <a href='https://github.com/rails-api/active_model_serializers/tree/v0.10.6/docs'>
        Guides
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href='https://github.com/rails-api/active_model_serializers/tree/0-9-stable'>0.9 (0-9-stable) Documentation
      </a>
    </td>
    <td>
      <a href='http://www.rubydoc.info/github/rails-api/active_model_serializers/0-9-stable'>
        <img src='http://img.shields.io/badge/yard-docs-blue.svg' />
      </a>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <a href='https://github.com/rails-api/active_model_serializers/tree/0-8-stable'>0.8 (0-8-stable) Documentation
      </a>
    </td>
    <td>
      <a href='http://www.rubydoc.info/github/rails-api/active_model_serializers/0-8-stable'>
        <img src='http://img.shields.io/badge/yard-docs-blue.svg' />
      </a>
    </td>
    <td></td>
  </tr>
</table>


## Status of AMS

### *Status*:

- ❗️ All existing PRs against master will need to be closed and re-opened against 0-10-stable, if so desired
- ❗️ Master, for the moment, won't have any released version of AMS on it.
- :eyes: See below for [alternatives](#alternatives)


### *Changes to 0.10.x maintenance*:

- The 0.10.x version has become a huge maintenance version.  We had hoped to get it in shape for a 1.0 release, but it is clear that isn't going to happen.  Almost none of the maintainers from 0.8, 0.9, or earlier 0.10 are still working on AMS. We'll continue to maintain 0.10.x on the 0-10-stable branch, but maintainers won't otherwise be actively developing on it.
  - We may choose to make a 0.11.x ( 0-11-stable) release based on 0-10-stable that just removes the deprecations.

### *What's happening to AMS*:

- There's been a lot of churn around AMS since it began back in [Rails 3.2](CHANGELOG-prehistory.md) and a lot of new libraries are around and the JSON:API spec has reached 1.0.
- If there is to be a 1.0 release of AMS, it will need to address the general needs of serialization in much the way ActiveJob can be used with different workers.
- The next major release *is* in development. We're starting simple and avoiding, at least at the outset, all the complications in AMS version, especially all the implicit behavior from guessing the serializer, to the association's serializer, to the serialization type, etc.
- The basic idea is that models to serializers are a one to many relationship.  Everything will need to be explicit.  If you want to serialize a User with a UserSerializer, you'll need to call it directly.  The serializer will essentially be for defining a basic JSON:API resource object: id, type, attributes, and relationships. The serializer will have an as_json method and can be told which fields (attributes/relationships) to serialize to JSON and will likely *not* know serialize any more than the relations id and type.  Serializing anything more about the relations would require code that called a serializer. (This is still somewhat in discussion).
- If this works out, the idea is to get something into Rails that existing libraries can use.

See [PR 2121](https://github.com/rails-api/active_model_serializers/pull/2121) where these changes were introduced for more information and any discussion.



## Alternatives

- [jsonapi-rb](http://jsonapi-rb.org/) is a [highly performant](https://gist.github.com/NullVoxPopuli/748e89ddc1732b42fdf42435d773734a) and modular JSON:API-only implementation.  There's a vibrant community around it that has produced projects such as [JSON:API Suite](https://jsonapi-suite.github.io/jsonapi_suite/).
- [fast_jsonapi](https://github.com/Netflix/fast_jsonapi) is a lightning fast JSON:API serializer for Ruby Objects from the team of Netflix.
- [jsonapi-resources](https://github.com/cerebris/jsonapi-resources) is a popular resource-focused framework for implementing JSON:API servers.
- [blueprinter](https://github.com/procore/blueprinter) is a fast, declarative, and API spec agnostic serializer that uses composable views to reduce duplication. From your friends at Procore.


For benchmarks against alternatives, see https://github.com/rails-api/active_model_serializers/tree/benchmarks



## Semantic Versioning

This project adheres to [semver](http://semver.org/)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)
