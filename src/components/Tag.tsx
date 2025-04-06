import React from 'react';

interface TagProps {
  name: string;
}

const Tag: React.FC<TagProps> = ({ name }) => {
  return (
    <span className="text-gray-600">
      &nbsp;&nbsp;[{name}]&nbsp;&nbsp;
    </span>
  );
};

export default Tag; 