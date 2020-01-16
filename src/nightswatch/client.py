from __future__ import absolute_import

from sentry.utils.http import absolute_uri
from sentry_plugins.client import ApiClient

INTEGRATION_API_URL = "https://paperduty.test.sre.cheanjia.net/v2/enqueue"


class NightsWatchClient(ApiClient):
    client = "sentry"
    plugin_name = "nightswatch"
    allow_redirects = False

    def __init__(self, service_key=None, api_url=None):
        self.service_key = service_key
        self.api_url = api_url
        super(NightsWatchClient, self).__init__()

    def build_url(self, path):
        return self.api_url if self.api_url else INTEGRATION_API_URL

    def request(self, data):
        payload = {"service_key": self.service_key}
        payload.update(data)

        return self._request(path="", method="post", data=payload)

    def trigger_incident(
        self,
        description,
        event_type,
        details,
        incident_key,
        client=None,
        client_url=None,
        contexts=None,
    ):
        return self.request(
            {
                "event_type": event_type,
                "description": description,
                "details": details,
                "incident_key": incident_key,
                "client": client or self.client,
                "client_url": client_url or absolute_uri(),
                "contexts": contexts,
            }
        )
