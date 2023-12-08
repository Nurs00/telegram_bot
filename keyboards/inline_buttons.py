from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration",
        callback_data="registration"
    )
    my_profile_button = InlineKeyboardButton(
        "My Profile",
        callback_data="my_profile"
    )
    random_profiles_button = InlineKeyboardButton(
        "View Profiles",
        callback_data="random_profiles"
    )
    reference_menu_button = InlineKeyboardButton(
        "Reference Menu",
        callback_data="reference_menu"
    )
    # supernatural_button = InlineKeyboardButton(
    #     "5 Season",
    #     callback_data="Supernatural_season"
    # )
    # O_service_button = InlineKeyboardButton(
    #     "O service",
    #     callback_data="service"
    # )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profiles_button)
    markup.add(reference_menu_button)
    # markup.add(supernatural_button)
    # markup.add(O_service_button)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Python",
        callback_data="python"
    )
    mojo_button = InlineKeyboardButton(
        "Mojo",
        callback_data="mojo"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like",
        callback_data=f"liked_profile_{owner_tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike",
        callback_data="random_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Update",
        callback_data=f"update_profile"
    )
    dislike_button = InlineKeyboardButton(
        "Delete",
        callback_data="delete_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_button = InlineKeyboardButton(
        "Reference Link",
        callback_data="reference_link"
    )
    reference_list_button = InlineKeyboardButton(
        "Reference List",
        callback_data="reference_list"
    )
    markup.add(reference_button)
    markup.add(reference_list_button)
    return markup

    # # noinspection PyUnreachableCode
    # async def save_button():
    #     markup = InlineKeyboardMarkup()
    #     save_service = InlineKeyboardButton(
    #         'save',
    #         call_back_data='save_service'
    #     )
    #     markup.add(save_service)
    #     return markup