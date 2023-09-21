import requests

cookies = {
    "JSESSIONID": "67F5C54B82C53EB4617E3320AC632888",
    "BIGipServernginxformobile": "636420618.50215.0000",
    "altmobile": "EX/2KxzlAgpLgt1AMEk1eg$$",
    "otsBusiness": "ERzEeRzlAgogewIDrfVbUQ$$",
}

headers = {
    "Host": "mobile.12306.cn",
    "nbappid": "60000001",
    "AppId": "9101430221728",
    "did": "Xq5jLHyWLM0DAM+t1DPmXsZp",
    "User-Agent": "MTPotal/1 CFNetwork/1390 Darwin/22.0.0",
    "Keep-Alive": "timeout=180, max=100",
    "tk": "e0MCDPVh2EoKkKSHU5_SLRnxNLkZfW_136j2j0",
    "uuid": "f412f117-f731-4a49-80da-5155e54e9a6c",
    "UniformGateway": "https://mobile.12306.cn/otsmobile/app/mds/mgw.htm",
    "bbid": "784202A3-0BCD-4CDA-B03F-057E3DCE73B7",
    "WorkspaceId": "product",
    "Platform": "IOS",
    "x-nb-appid": "AP_60000001_ios",
    "Connection": "Keep-Alive",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "fo": "pk6cv1j41av7b8ruCphSJ2qS0YV-kbqqR2hXya933Rc0YGmSf2LwFz2M4Owgh8LwJS5XGV0p2UOvd1XX591IVLvasLNRBos1eQiS-SbwCNLj1k9sujuV6xdFLvg",
    "nbversion": "5.7.1.43",
}

params = {
    "operationType": "com.cars.otsmobile.queryLeftTicketZ",
    "requestData": '[{"train_date":"20231004","purpose_codes":"00","from_station":"CBQ","to_station":"HZH","station_train_code":"","start_time_begin":"0000","start_time_end":"2400","train_headers":"QB#","train_flag":"","seat_type":"0","seatBack_Type":"","ticket_num":"","dfpStr":"","baseDTO":{"time_str":"20230920193731","os_type":"i","mobile_no":"","device_no":"9C11FC19765E4A2E8B96DC2C3BF47A7F","h5_app_id":"60000001","user_name":"jsc886","check_code":"c1bf257331e4fa42c77f23529d902983","h5_app_version":"5.7.1.43","version_no":"5.7.4.1"}}]',
    "ts": "OgoOOZY",
    "sign": "1e1d7e7e19f98885e3db98eea5320abd",
}

response = requests.get(
    "https://mobile.12306.cn/otsmobile/app/mgs/mgw.htm",
    params=params,
    cookies=cookies,
    headers=headers,
)
if response.json().get("resultStatus") == 1000:
    tickets = response.json().get("result").get("ticketResult")
    for ticket in tickets:
        if ticket.get("station_train_code") == "D908":
            # 车次
            station_train_code = ticket.get("station_train_code")
            # 信息 ---- 列车运行图调整,暂停发售
            controlled_train_message = ticket.get("controlled_train_message")
            if controlled_train_message == "列车运行图调整,暂停发售":
                msg = station_train_code + "车次,没有开售"
                print(msg)
            else:
                msg = station_train_code + "车次,已开售"
                print(msg)
                # 发送通知
                response = requests.post(
                    url="https://wxpusher.zjiecode.com/api/send/message",
                    json={
                        "appToken": "AT_3n08Q4TBgpoJxPxwWqUHHgv9xLY1Nubk",
                        "content": "聪聪提醒:潮汕上头行之回城 " + msg,
                        "contentType": 1,
                        "topicIds": [22628],
                        "verifyPay": "false",
                    },
                    headers={"Content-Type": "application/json"},
                )
                if response.json().get("code") == 1000:
                    print("发送通知成功")
                else:
                    print(response.json().get("msg"))
