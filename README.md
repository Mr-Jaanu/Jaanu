# Save Restricted Bot

*A Telegram Bot, Which can send you restricted content by it's post link with <b>login feature</b>*

---

## Variables

- `API_HASH` : fd9b06421885c66f99587917f4127df1
- `API_ID` : 26625764
- `BOT_TOKEN` : 8197756021:AAEY4cmnK6BiwFgNs1peo4o3MjtvnOxHzOA
- `ADMINS` : Your Admin Id For Broadcasting Message
- `DB_URI` : Your Mongodb Database Url From [Mongodb](https://mongodb.com) Watch [Video Tutorial](https://youtu.be/DAHRmFdw99o) ( Warning - Give Db uri in deploy server environment variable, don't give in repo )
- `ERROR_MESSAGE` : Set True Or False, If You Want Error Message Then True Else False.

---

## Commands

- `/start` : Check Bot Is Working Or Not
- `/help` : Check How To Use Bot
- `/login` : Login Your Telegram String Session 
- `/logout` : Logout Your Session 
- `/cancel` : Cancel Your Any Ongoing Task
- `/broadcast` : Broadcast Message To User (Admin Only)

---

## Usage

__FOR PUBLIC CHATS__

_just send post/s link_


__FOR PRIVATE CHATS__

_first send invite link of the chat (unnecessary if the account of string session already member of the chat)
then send post/s link_


__FOR BOT CHATS__

_send link with '/b/', bot's username and message id, you might want to install some unofficial client to get the id like below_

```
https://t.me/b/botusername/4321
```

__MULTI POSTS__

_send public/private posts link as explained above with formate "from - to" to send multiple messages like below_


