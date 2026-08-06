## Gemini Chat Model Response

```js
Interaction(
│   status='completed',
│   model='gemini-3.6-flash',
│   agent=None,
│   id='v1_Chd1eWQwYW9UU0E4YXFqdU1QemJDNmdROBIXd',
│   created='2026-08-06T06:20:43Z',
│   updated='2026-08-06T06:20:43Z',
│   system_instruction=None,
│   tools=None,
│   usage=Usage(
│   │   cached_tokens_by_modality=None,
│   │   grounding_tool_count=None,
│   │   input_tokens_by_modality=[ModalityTokens(modality='text', tokens=7)],
│   │   output_tokens_by_modality=None,
│   │   tool_use_tokens_by_modality=None,
│   │   total_cached_tokens=0,
│   │   total_input_tokens=7,
│   │   total_output_tokens=21,
│   │   total_thought_tokens=373,
│   │   total_tokens=401,
│   │   total_tool_use_tokens=0
│   ),
│   response_modalities=None,
│   response_mime_type=None,
│   previous_interaction_id=None,
│   environment_id=None,
│   service_tier='standard',
│   webhook_config=None,
│   steps=[
│   │   ThoughtStep(
│   │   │   signature='EtELCs4LARFNMg9max48h+7zcTw/tHSvTjdzqrsvqRBZAY378O/3Vrd/1aBUQqOOfBmZq7OqPOVBYhyMRRAHjcVVI+ZnX17h/KSmSJfBAjIeprG+L6iksn8h3OkVbPTqTAZo+sGNC5xtJZfBgwyCDHcIamcbbHJQCjw55o0jDVg6RY92pe7k1Wbsu58Mq0k6bGx8CVGDTrLflm48JUNPteyBMwJcNEyckCSY4xdMj2zJtp/AXsXAyKHEmJWmWc4goP/',
│   │   │   summary=None,
│   │   │   type='thought'
│   │   ),
│   │   ModelOutputStep(
│   │   │   content=[
│   │   │   │   TextContent(
│   │   │   │   │   text='Money is a universally accepted tool used to measure, store, and trade the value of goods and services.',
│   │   │   │   │   annotations=None,
│   │   │   │   │   type='text'
│   │   │   │   )
│   │   │   ],
│   │   │   error=None,
│   │   │   type='model_output'
│   │   )
│   ],
│   response_format=None,
│   environment=None,
│   generation_config=None,
│   agent_config=None,
│   safety_settings=None,
│   labels=None,
│   input=None,
│   output_text='Money is a universally accepted tool used to measure, store, and trade the value of goods and services.',
│   output_image=None,
│   output_audio=None,
│   output_video=None,
│   object='interaction'
)
```

## Chatgpt Chat Model Response

```js
ChatCompletion(
│   id='chatcmpl-2ff0f317-d3ee-b96cf04677a0',
│   choices=[
│   │   Choice(
│   │   │   finish_reason='stop',
│   │   │   index=0,
│   │   │   logprobs=None,
│   │   │   message=ChatCompletionMessage(
│   │   │   │   content='Kubernetes is an open-source container orchestration system that automates the deployment, scaling, and management of containerized applications across a cluster of machines.',
│   │   │   │   refusal=None,
│   │   │   │   role='assistant',
│   │   │   │   annotations=None,
│   │   │   │   audio=None,
│   │   │   │   function_call=None,
│   │   │   │   tool_calls=None
│   │   │   )
│   │   )
│   ],
│   created=1786022989,
│   model='llama-3.3-70b-versatile',
│   object='chat.completion',
│   moderation=None,
│   service_tier='on_demand',
│   system_fingerprint='fp_3272ea2d91',
│   usage=CompletionUsage(
│   │   completion_tokens=31,
│   │   prompt_tokens=42,
│   │   total_tokens=73,
│   │   completion_tokens_details=None,
│   │   prompt_tokens_details=None,
│   │   queue_time=0.162515338,
│   │   prompt_time=0.001943196,
│   │   completion_time=0.045823085,
│   │   total_time=0.047766281
│   ),
│   usage_breakdown=None,
│   x_groq={'id': 'req_01kzbm835ce4vrag0b01b7rg3e', 'seed': 1031643070}
)
```
