# :running: WIP

## Introduction

[中文文档](README.zh.md)
llm-runtime encapsulates the runtime of various models and provides a simple abstract interface for easy deployment.



## Diagram

```mermaid
graph LR

create-->llm_runtime
destroy-->llm_runtime
process-->llm_runtime
llm_runtime-->llamaRT
llm_runtime-->samRT
llm_runtime-->sdRT
llm_runtime-->ctrlnetRT
```

## Support plan

- [ ] LLama
- [ ] SAM(meta)
- [ ] Stable Diffusion
- [ ] Control Net
