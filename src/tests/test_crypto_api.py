from webapp.crypto_api import transform, get_response
import types


def test_transform():
    test_fake_data = {
   
        "data": {
            "BTC": [
                    {
                        "id": 1,
                        "name": "Bitcoin",
                        "symbol": "BTC",
                            "quote": {
                            "USD": {
                                    "price": 103929.32609335119,
                                
                                }
                        }
                    },
            ]
        }
    }
    result = transform(test_fake_data)
 

def test_response(monkeypatch):
    class DummyResp:
        status_code = 200
        url = "https://example.com"
        def raise_for_status(self): pass
        def json(self):
            return {
                "data": {
                    "BTC": [
                        {
                            "symbol": "BTC",
                            "quote": {"USD": {"price": 12345.67}}
                        }
                    ]
                }
            }

    def fake_get(url, headers=None, params=None, timeout=10):
        return DummyResp()

    monkeypatch.setattr("webapp.crypto_api.requests.get", fake_get)

    resp = get_response()
    assert resp.status_code == 200

    result = transform(resp.json())
    assert result["symbol"] == "BTC"
    assert result["price"] == 12345.67

    

    
    


