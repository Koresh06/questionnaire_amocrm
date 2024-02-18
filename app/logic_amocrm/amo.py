from amocrm.v2 import tokens
from amocrm.v2 import Lead as _Lead, custom_field

# tokens.default_token_manager(
#     client_id="93982ff0-0a95-45c8-b05f-a7e524866766",
#     client_secret="KnTE4Ae9HBfxAbNlcNEjFN6LNxYKK9VK1Mg3lIq5B5Jvnt8FQfgyLDjcXGB3BUkn",
#     subdomain="digitalwomenclub",
#     redirect_url="https://t.me/digitalwomen_bot",
#     storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
#     )
#tokens.default_token_manager.init(code="def502000e0e465bc7e1904f6e6ab0138d50d397bddbed5904d0adef985a489d35fdc1e6959038f801e4a2a32f43fc9a6e48b2dbd1a1b30aa12d6e7eda88337d39d20e5ce51dcc56c3626121248d9f3fff5b25458539b11525c83778a6ac90cd89baab52eb660a53132c455fb02d3317c39d4bee69585e984bdfc2c1ada9be8083d93472d6d7118348daec1b8314fee954c56a7b9009fc5357e4136422acd9d1b74f71f57fd6097d3eb131cd4a9e53d284313753f6f2980b5fa002b809ee5db8309e4c47c19f1c8746f55e2e3e385f71214b556cff95872cccadac380e308891d284ddab3df64a26237d559727c7079cf63abda037d091e831db0e0c9081f78f0d1c51b547793fa890bab9f2716ada079c4df6b6647908013377c6f6e0a72cca3f9d32bd7c665fc204ca60db0e06b6d956675b472095f94f51c71c58827bb1a00a94848da24ff491620de212c2470ffc806506cb975b4b6f7b29ea22284ff8efda4c2711112228b047f4518c66daab71928a162750192b5e41ed1ef7d185123e16d0a36915c25a66555dcebfa6006f0616348313afb1abefe0347769ebbee8dfdb59556b8dd9caf8ee5b8774b782f8be96c709206e97dc501b0bdac62b9fffaf52838cf792cef269ab5135608df2fa62e1b90619075efb4d81ce9170571fdaf7ae50accdf2d713eecaced58f0c9d", skip_error=False)

class Lead(_Lead):
    tg_id = custom_field.TextCustomField("ID_телеграмм")
    username_tg = custom_field.TextCustomField("Имя в телеграмме")
    phone = custom_field.TextCustomField("Телефон")
    inst = custom_field.TextCustomField("Инстаграм")
    descriphion = custom_field.TextCustomField("Описание")

async def save_custom_field(tg_id, username_tg, data):
    try:
        lead = Lead.objects.create(data={
            'name': data['name'],
        })
        lead.tg_id = tg_id
        lead.username_tg = username_tg
        lead.phone = data['telephone']
        lead.inst = data['inst']
        lead.descriphion = data['descriphion']
        lead.save()
        return True
    except Exception as exxit:
        print(exxit)
        return False


