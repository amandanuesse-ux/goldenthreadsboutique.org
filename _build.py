import re
head=open('_head.html').read(); foot=open('_foot.html').read()
pages={
 'request.html':('_request.html','Request a boutique | Golden Threads Boutique','Request a Golden Threads traveling boutique at your senior living community, or recommend a community you love.','request.html'),
 'give.html':('_give.html','Give | Golden Threads Boutique','Give money or clothing to the Golden Threads Giving Program and provide shopping credits for seniors in need.','give.html'),
 'contact.html':('_contact.html','Contact | Golden Threads Boutique','Contact Golden Threads Boutique about boutique visits, giving, donating clothing or volunteering.','contact.html'),
 'thanks.html':('_thanks.html','Thank you | Golden Threads Boutique','Thank you for contacting Golden Threads Boutique.',None),
}
for out,(body,title,desc,cur) in pages.items():
    h=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',head)
    h=re.sub(r'<meta name="description" content=".*?">',f'<meta name="description" content="{desc}">',h)
    h=h.replace(' aria-current="page"','')
    if cur:
        h=h.replace(f'href="{cur}">',f'href="{cur}" aria-current="page">',1)
    open(out,'w').write(h+open(body).read()+foot)
print('built')
