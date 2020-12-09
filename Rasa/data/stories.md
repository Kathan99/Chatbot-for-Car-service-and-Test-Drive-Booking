## survey old customer registration
*greet
    - utter_greet
    - utter_help
*serviceneed
    - utter_question
*affirm
    - service
    - form{"name":"service"}
    - form{"name":null}
    - action_restart

## survey  customer registration
*greet
    - utter_greet
    - utter_help
*serviceneed
    - utter_question
*deny
    - utter_start_register
*affirm
    - submission
    - form{"name":"submission"}
    - form{"name":null}
    - action_restart
    
## survey  stop
*greet
    - utter_greet
    - utter_help
*serviceneed
    -utter_question
*deny
    - utter_start_register
*affirm
    - submission
    - form{"name":"submission"}
*out_of_scope
    - utter_ask_continue
*deny
    - action_deactivate_form
    - form{"name":null}
    - action_restart
    
## survey  continue
*greet
    - utter_greet
    - utter_help
*serviceneed
    -utter_question
*deny
    - utter_start_register
*affirm
    - submission
    - form{"name":"submission"}
*out_of_scope
    - utter_ask_continue
*confirm
    - submission
    - form{"name":"submission"}
    - form{"name":null}
    - action_restart
    
## survey deny service
*greet
    - utter_greet
    - utter_help
*deny
    - utter_great_day
    - action_restart
    
## survey direct suvbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsuv
    - utter_ecosport
    - utter_endeavour
    - utter_explorer
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}
    - action_restart
    
## survey ask suvbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsuv
    - utter_ecosport
    - utter_endeavour
    - utter_explorer
*carselect{"testcar":"Figo"}
    - slot{"testcar":"Figo"}
    - testdrive
    - slot{"testcar":null}
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}
    - action_restart
    
## survey deny suvbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsuv
    - utter_ecosport
    - utter_endeavour
    - utter_explorer
*deny
    - utter_good_day
    - action_restart
    
## survey deny after asking suvbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsuv
    - utter_ecosport
    - utter_endeavour
    - utter_explorer
*carselect{"testcar":"Figo"}
    - slot{"testcar":"Figo"}
    - testdrive
    - slot{"testcar":null}
*deny
    - utter_good_day
    - action_restart

## survey stop suvbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsuv
    - utter_ecosport
    - utter_endeavour
    - utter_explorer
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
*out_of_scope
    - utter_ask_continue
*deny
    - action_deactivate_form
    - form{"name":null}
    - action_restart

## survey continue suvbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsuv
    - utter_ecosport
    - utter_endeavour
    - utter_explorer
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
*out_of_scope
    - utter_ask_continue
*confirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}    
    - action_restart

## survey direct sedanbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsedan
    - utter_aspire
    - utter_focus
    - utter_mustang
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}
    - action_restart
      
## survey ask sedanbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsedan
    - utter_aspire
    - utter_focus
    - utter_mustang
*carselect{"testcar":"Figo"}
    - slot{"testcar":"Figo"}
    - testdrive
    - slot{"testcar":null}
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}
    - action_restart
    
## survey deny sedanbook 
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsedan
    - utter_aspire
    - utter_focus
    - utter_mustang
*deny
    - utter_good_day
    - action_restart
    
## survey deny after asking sedanbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsedan
    - utter_aspire
    - utter_focus
    - utter_mustang
*carselect{"testcar":"Figo"}
    - slot{"testcar":"Figo"}
    - testdrive
    - slot{"testcar":null}
*deny
    - utter_good_day
    - action_restart
    
## survey stop sedanbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsedan
    - utter_aspire
    - utter_focus
    - utter_mustang
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
*out_of_scope
    - utter_ask_continue
*deny
    - action_deactivate_form
    - form{"name":null}
    - action_restart
    
## survey continue sedanbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarsedan
    - utter_aspire
    - utter_focus
    - utter_mustang
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
*out_of_scope
    - utter_ask_continue
*confirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}    
    - action_restart
    
## survey direct hatchbackbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarhatchback
    - utter_figo
    - utter_freestyle
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}
    - action_restart
    
## survey ask hatchbackbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarhatchback
    - utter_figo
    - utter_freestyle
*carselect{"testcar":"Figo"}
    - slot{"testcar":"Figo"}
    - testdrive
    - slot{"testcar":null}
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}
    - action_restart
    
## survey deny hatchbackbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarhatchback
    - utter_figo
    - utter_freestyle
*deny
    - utter_good_day
    - action_restart
    
## survey deny after asking hatchbackbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarhatchback
    - utter_figo
    - utter_freestyle
*carselect{"testcar":"Figo"}
    - slot{"testcar":"Figo"}
    - testdrive
    - slot{"testcar":null}
*deny
    - utter_good_day
    - action_restart
    
## survey stop hatchbackbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarhatchback
    - utter_figo
    - utter_freestyle
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
* out_of_scope
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name":null}
    - action_restart
    
## survey continue hatchbackbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarhatchback
    - utter_figo
    - utter_freestyle
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
*out_of_scope
    - utter_ask_continue
*confirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}    
    - action_restart
    
## survey direct crossoverbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarcrossover
    - utter_edge
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}
    - action_restart
    
## survey ask crossoverbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarcrossover
    - utter_edge
*carselect{"testcar":"Figo"}
    - slot{"testcar":"Figo"}
    - testdrive
    - slot{"testcar":null}   
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}
    - action_restart
    
## survey deny crossoverbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarcrossover
    - utter_edge
*deny
    - utter_good_day  

## survey deny after asking crossoverbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarcrossover
    - utter_edge
*carselect{"testcar":"Figo"}
    - slot{"testcar":"Figo"}
    - testdrive
    - slot{"testcar":null}
*deny
    - utter_good_day
    - action_restart
    
## survey stop crossoverbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarcrossover
    - utter_edge
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
*out_of_scope
    - utter_ask_continue
*deny
    - action_deactivate_form
    - form{"name":null}    
    - action_restart
    
## survey continue crossoverbook
*greet
    - utter_greet
    - utter_help
*testdriveneed
    - utter_car_types
*testcarcrossover
    - utter_edge
*confirmation
    - utter_great_news
    - utter_start_book
*affirm
    - testbook
    - form{"name":"testbook"}
*out_of_scope
    - utter_ask_continue
*confirm
    - testbook
    - form{"name":"testbook"}
    - form{"name":null}    
    - action_restart
      
## bot challenge
*bot_challenge
    - utter_iamabot
    - action_restart
