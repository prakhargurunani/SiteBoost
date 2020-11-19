import PyPSI
import urllib3

http = urllib3.PoolManager()

def PSI(url, category="performance", locale="en", stratergy="desktop", utm_campaign="", utm_source="", captcha_token=""):
    if "https" in url:
        return(http.request('GET', 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token).data)
    if "http" in url:
        return(http.request('GET', 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token).data)
    else:
        site_url = "http://" + url
        return(http.request('GET', 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + site_url + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token).data)