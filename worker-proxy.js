async function handleRequest(event, website) {
  if (website == null) {
    website = 'https://scaredos.me/'
  } else {
    website = website + '/' + event.request.url.split('/')[3]
  }
  const headers = {
    headers: {
      "host": website,
      "user-agent": "Mozilla/5.0"
    }
  }
  const response = await fetch(website, headers)
  return response
}

addEventListener("fetch", event => {
  var website = event.request.headers.get('Website');
  return event.respondWith(handleRequest(event, website))
})
