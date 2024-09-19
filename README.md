
#  User subscription

user subscription project let user subscribe using email id. also it let user to select plan for subscription like which plan user wants to take.user can activate and deativate plan.





## How to run the project

create virtual environment with below command

```bash
  python -m venv subscription
```

Activate virtual environment running below command

```bash
  .\subscription\scripts\activate.bat
```
Install libraries from requirements.txt with below command

```bash
  pip install -r requirements.txt
```
run main.py using below command

```bash
  python main.py
```

## Files introduction



| Name             | description                                                                |
| ----------------- | ------------------------------------------------------------------ |
| main.py | main file that contains all the api endpoints and crud operations |
| database.py | this files contains all db configuration |
| models.py | this file contains table name and its fields and schema |

## API Reference

#### Get all user subscription

```http
  GET /all_user_subscription
```

 | Description                |
 | :------------------------- |
| this endpoint will return all subscribed user list |




#### home page to subscribe user by filling details

```http
  GET/POST  /
```

 | Description                |
 | :------------------------- |
| enter user details to subscribe user |


#### Check user subscription by providing email address

```http
  GET /subscription_status/<email>
```

 | Description                |
 | :------------------------- |
| this endpoint will return provided user subscription |

#### activate and deactivate user subscription

```http
  GET /update_subs/<email>
```

 | Description                |
 | :------------------------- |
| make subscription activate and deactivate |



#### unsubscribe subscribed user

```http
  GET /unsubscribe/<email>
```

 | Description                |
 | :------------------------- |
| unsubscribe subscribed user with email |

