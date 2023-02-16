
## Level 1 - task 3
> a1qa study project

Using Selenium and python (pytest) to work with specific elements such as alerts, iframes, tables, sliders, new tabs and windows etc. on [demoqa.com ](https://demoqa.com/) page. Simple framework implementing page object model with base forms, singleton driver, browser factory, logging and parametrized tests (basic data driven testing).


#### test case 1 - Alerts

|  step | expected result  |
| ------------ | ------------ |
|  Navigate to main page | Main page is open  |
| Click on Alerts, Frame & Windows button <br> In a menu click Alerts button  | Alerts form has appeared on page  |
| Click on 'Click Button to see alert' button  | Alert with text "You clicked a button" is open  |
| Click OK button  | alert has closed  |
| Click on 'On button click, confirm box will appear' button | Alert with text "Do you confirm action?" is open |
| Click on OK button | Alert has closed <br> text "You selected Ok" has appeared on page |
|Click on "On button click, prompt box will appear" button|  Alert with text "Please enter your name" is open|
|Enter randomly generated text, click OK button| Alert has closed <br> Appeared text equals to the one you've entered before |


#### test case 2 - Iframe

| step  | expected result   |
| ------------ | ------------ |
|Navigate to main page|main page is open|
|Click on Alerts, Frame & Windows button;<br> In a menu click Nested Frames button| Page with Nested Frames form is open;<br> There are messages "Parent frame" & "Child Iframe" present on page|
|Select Frames option in a left menu| Page with Frames form is open;<br> Message from upper frame is equal to the message in lower frame|


#### test case 3 - Tables
| step  | expected result   |
| ------------ | ------------ |
|Navigate to main page|main page is open|
|Click on Elements button; In the menu click a Web Tables button| Page with Web Tables form is open|
|Click on Add button|Registration Form has appeared on page|
|Enter predefined data for User then click Submit button| Registration form has closed;<br>Data of the User has appeared in the table|
|Click Delete button in a row which contains data of User| Number of records in table has changed;<br> Data of User has been deleted from table|

#### test case 4 - Windows and tabs
| step  | expected result   |
| ------------ | ------------ |
|Navigate to main page|main page is open|
|Click on Alerts, Frame & Windows button; In the menu click a Browser Windows button| Page with Browser Windows form is open|
|Click on New Tab button| New tab with sample page is open|
|Close current tab|Page with Browser Windows form is open|
|In the menu on the left click Elements → Links button|Page with Links form is open|
|Click on Home link|New tab with main page is open|
|Resume to previous tab|Page with Links form is open|

#### test case 5 - sliders and progress bar
| step  | expected result   |
| ------------ | ------------ |
|Navigate to main page|main page is open|
|Click on Widgets button. In the menu on the left click Slider button|Page with Slider form is open|
|Set slider to a valid randomly generated value| Value on the page near the slider is equals to the one set before|
|In the left menu click Progress Bar button|Page with Progress Bar form is open|
|Click on Start button| - |
|Click on Stop button, when value displayed on progress bar becomes equals to previously generated random number|Value on progress bar is equal to generated number (error is not higher than 2 %)|
