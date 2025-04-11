import Editor from '@monaco-editor/react';
import { useEffect, useState } from 'react';

interface Props {
  initialCode: string;
  onCodeChange: (value: string) => void;
}

export default function CodeEditor({ initialCode, onCodeChange }: Props) {
  const [code, setCode] = useState(initialCode);

  useEffect(() => {
    setCode(initialCode);
  }, [initialCode]);

  return (
    <Editor
      height="300px"
      defaultLanguage="python"
      value={code}
      theme="vs-dark"
      onChange={(value) => {
        const updated = value || '';
        setCode(updated);
        onCodeChange(updated);
      }}
    />
  );
}
