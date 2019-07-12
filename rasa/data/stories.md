## happy path
* get_started
  - utter_intro
* say_name
  - action_save_name
  - utter_name
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* get_started
  - utter_intro
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* get_started
  - utter_intro
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* get_started
  - utter_intro
* goodbye
  - utter_goodbye
