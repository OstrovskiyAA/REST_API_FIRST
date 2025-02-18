post_users = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "id": {
            "type": "string"
        }
    },
    "required": [
        "name",
        "job",
        "id"
    ]
}

post_user_2 = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "year": {
          "type": "integer"
        },
        "color": {
          "type": "string"
        },
        "pantone_value": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name",
        "year",
        "color",
        "pantone_value"
      ]
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    }
  },
  "required": [
    "data",
    "support"
  ]
}