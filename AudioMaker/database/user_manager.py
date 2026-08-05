from database.database import (
    get_user,
    create_user
)

def get_current_account(
        discord_user=None,
        visitor_id=None
):

    # User with Login

    if discord_user:

        user = get_user(
        discord_user["id"]
        )



        if not user:

           create_user(
              discord_id=discord_user["id"],
              username=discord_user["global_name"]

           )

           user = get_user(
               discord_user["id"]
           )

        return {
            "type": "discord",
            "id": discord_user["id"],
            "data": user
        }

    # User without login

    else:

        user = get_user(
           visitor_id
        )

        if not user:

           create_user(
              visitor_id=visitor_id
           )

           user = get_user(
              visitor_id
           )

        return {
           "type": "visitor",
           "id": visitor_id,
           "data": user
        }