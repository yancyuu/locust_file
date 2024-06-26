from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://dify.lazygpt.cn/app/8d21e202-50c1-41ec-98d0-ec9697449e9b/configuration',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzRiNmI5ODgtMmIyMC00ODFmLTk0MzUtY2JkOThiZDdkMGE4IiwiZXhwIjoxNzIxODc5MzIwLCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.f3PF7YuaFqRG',
        'content-type': 'application/json'
    }

    @task(1)
    def post_chat_message(self):
        self.client.post(
            "/console/api/apps/8d21e202-50c1-41ec-98d0-ec9697449e9b/chat-messages",
            headers=self.headers,
            json={
                "response_mode": "streaming",
                "conversation_id": "",
                "query": "dads",
                "inputs": {},
                "model_config": {
                    "pre_prompt": "## 知识库所有信息都是SKG健康科技公司的信息，必须用中文回答用户问题，回答问题需要联系上下文；\n## 先引导用户说出产品名称，根据产品名称回答问题，不要自己瞎猜产品名称;\n## 当用户只提及产品型号时，请优先引导用户说出自己的需求；\n## 当用户问产品区别的时候需要具体准确，输出每一个差异点，并且将产品图片链接也作为区别输出；\n## 当问题以及上下文和知识库中的内容不相符或无关时，告诉用户你不知道相关信息，同时推荐来自于知识库的相似的产品信息，若没有则不推荐，不可欺骗用户；\n## 产品信息，地址，电话号码知识库没有就回答不知道，切记不可乱编；\n## 扮演一家名为SKG健康科技公司的首席健康专家小S，你将根据文档中信息进行回答，不要精简答案；\n## 你可以输出视频和图片，如果给定的知识库答案中存在图片、视频、文件等链接，需要将图片链接全部输出。\n## 链接千万不要使用markdown格式渲染输出，直接将原始链接进行输出;\n## 你负责处理用户对于产品的问题，并为用户进行解答，当用户问题只涉及型号时，优先给出知识库中对应型号的卖点功能的完整文档信息并梳理逻辑，核心点分段落发出;\n## 当用户说哪个部位有问题或某种症状时，请你担任康复专家和脉冲理疗专家向他解释这种病症的发病原因和表现，以及脉冲加热敷对这种症状的影响；\n## 你的回复要人性化，运用更多的语气助词，模仿真人进行回复，分类分段输出，像个小女生一样，使用丰富的符号表情;\n## 当用户说某节日发朋友圈时，尽量将他所提产品的功能卖点加上节日文案库中对应的节日诗句选择一句做开头输出；\n## 拒绝回答有关政治，宗教，饭圈文化，娱乐圈有关问题。\n## 如果用户提出退货退款相关信息，直接告诉用户联系购买平台上的商家。\n## 如果知识库信息和你以往的经验都没有解决用户问题，那么引导用户转人工客服：400-8220888。",
                    "prompt_type": "simple",
                    "chat_prompt_config": {},
                    "completion_prompt_config": {},
                    "user_input_form": [],
                    "dataset_query_variable": "",
                    "opening_statement": "",
                    "more_like_this": {"enabled": False},
                    "suggested_questions": [],
                    "suggested_questions_after_answer": {"enabled": True},
                    "text_to_speech": {"enabled": True, "language": "zh-Hans", "voice": "echo"},
                    "speech_to_text": {"enabled": True},
                    "retriever_resource": {"enabled": True},
                    "sensitive_word_avoidance": {"enabled": False, "type": "", "configs": []},
                    "agent_mode": {"enabled": False, "max_iteration": 5, "strategy": "function_call", "tools": []},
                    "dataset_configs": {
                        "retrieval_model": "multiple",
                        "top_k": 10,
                        "score_threshold": 0.5,
                        "reranking_model": {"reranking_provider_name": "nvidia", "reranking_model_name": "nv-rerank-qa-mistral-4b:1"},
                        "datasets": {"datasets": [{"dataset": {"enabled": True, "id": "11cbc188-d4d5-471a-8606-3d6faaf53b31"}}, {"dataset": {"enabled": True, "id": "19abe3f0-9dd3-47ed-a115-8ce437decb04"}}]}
                    },
                    "file_upload": {"image": {"enabled": False, "number_limits": 3, "detail": "high", "transfer_methods": ["remote_url", "local_file"]}},
                    "annotation_reply": {"id": "aafd1159-08f4-47a0-93f5-caf5c2f2af7c", "enabled": True, "score_threshold": 0.8, "embedding_model": {"embedding_provider_name": "azure_openai", "embedding_model_name": "text-embedding-ada-002"}},
                    "supportAnnotation": True,
                    "appId": "8d21e202-50c1-41ec-98d0-ec9697449e9b",
                    "supportCitationHitInfo": True,
                    "model": {"provider": "volcengine_maas", "name": "Doubao-pro-32k", "mode": "chat", "completion_params": {"stop": []}}
                }
            }
        )

    @task(2)
    def get_chat_messages(self):
        self.client.get(
            "/console/api/apps/8d21e202-50c1-41ec-98d0-ec9697449e9b/chat-messages?conversation_id=e900ccd0-f14d-4206-9d08-abb36b9c0f06",
            headers=self.headers
        )

    @task(3)
    def get_suggested_questions(self):
        self.client.get(
            "/console/api/apps/8d21e202-50c1-41ec-98d0-ec9697449e9b/chat-messages/ff24fcd7-eae0-410e-a2c9-0a47af969551/suggested-questions",
            headers=self.headers
        )

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://dify.lazygpt.cn"