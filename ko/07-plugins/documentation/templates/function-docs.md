<!-- i18n-source: 07-plugins/documentation/templates/function-docs.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: source-copy -->
<!-- i18n-date: 2026-10-26 -->

# Function: `functionName`

## Description
Brief description of what the function does.

## Signature
```typescript
function functionName(param1: Type1, param2: Type2): ReturnType
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| param1 | Type1 | Yes | Description of param1 |
| param2 | Type2 | No | Description of param2 |

## Returns
**Type**: `ReturnType`

Description of what is returned.

## Throws
- `Error`: When invalid input is provided
- `TypeError`: When wrong type is passed

## Examples

### Basic Usage
```typescript
const result = functionName('value1', 'value2');
console.log(result);
```

### Advanced Usage
```typescript
const result = functionName(
  complexParam1,
  { option: true }
);
```

## Notes
- Additional notes or warnings
- Performance considerations
- Best practices

## See Also
- [Related Function](#)
- [API Documentation](#)

---

**Last Updated**: August 4, 2026
**Claude Code Version**: 2.1.220
**Sources**:
- https://code.claude.com/docs/en/plugins
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
