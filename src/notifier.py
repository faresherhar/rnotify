from utils.renderer import render_notification

content = render_notification(
    provider="gitlab",
    repo="AuroraOSS/AuroraStore",
    release_name="3.2.8",
    tag_name="3.2.8",
    type="txt",
)

print(content)
