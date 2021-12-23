actions = {}
for user, crontabs in node.metadata.get('crontab', {}).items():
    crontabContent = ""
    for ct in crontabs:
        crontabContent += f"{ct.get('minute', '*')} {ct.get('hour', '*')} {ct.get('dayOfMonth', '*')} " \
                          f"{ct.get('month', '*')} {ct.get('dayOfWeek', '*')} {ct.get('command')}\n"

    actions[f"crontab_for_{user}"] = {
        'command': f'echo "{crontabContent}" | sudo crontab -u {user} -',
        'unless': f'test "$(crontab -l)" -eq "{crontabContent}"',
    }
